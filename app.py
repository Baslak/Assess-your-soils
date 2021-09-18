from re import template
from database import sql_select, sql_write
from models.users import login_check
from models.vineyards import add_vineyard, vineyard_check, delete_vineyard, update_vineyard, amend_vineyard
from models.calculator import check_spray

from flask import Flask, request, render_template, redirect, session
from email.utils import parseaddr

import psycopg2
import bcrypt
import os

DB_URL = os.environ.get("DATABASE_URL", "dbname=vinproof_db")
SECRET_KEY = os.environ.get("SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def homepage():
    user_id = session.get('user_id')
    user_object = login_check(user_id)

    return render_template('base.html', user_id=user_id, user_object=user_object)

@app.route('/login')
def login():
    user_id = session.get('user_id')
    user_object = login_check(user_id)

    return render_template('login.html', user_object=user_object)

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/login_confirm', methods=['POST'])
def login_confirm():
    user_id = session.get('user_id')
    user_object = login_check(user_id)

    email = request.form.get('email')
    password = request.form.get('password')

    user_info = sql_select("SELECT id, full_name, company, email, password_hash FROM users WHERE email = %s", [email])
    
    if email == "" or len(user_info) == 0:
        no_strings_attached = 'No dice, i need strings!'
        return render_template('login.html', no_strings_attached=no_strings_attached, user_object=user_object)
    else: 
        password_hash = user_info[0][4]
        valid = bcrypt.checkpw(password.encode(), password_hash.encode())

        if valid:
            print('You are in!')
            session['full_name'] = user_info[0][1]
            session['company'] = user_info[0][2]
            session['email'] = user_info[0][3]
            session['user_id'] = user_info[0][0]
            session['password_hash'] = user_info[0][4]
            return redirect('/')
        else:
            return redirect('/login')
        
@app.route('/signup')
def signup():
    user_id = session.get('user_id')

    if user_id == None:
        user_object = login_check(user_id)
        return render_template('signup.html', user_object=user_object)
    else:
        user_object = login_check(user_id)
        return render_template('login.html', user_object=user_object)

@app.route('/signup_action', methods=['POST'])
def signup_action():
    user_id = session.get('user_id')
    user_object = login_check(user_id)

    full_name = request.form.get('full_name')
    company = request.form.get('company')
    email = request.form.get('email')
    password = request.form.get('password')

    if parseaddr(str(email)) and '@' in email:
        print('valid email')

        user = sql_select('SELECT id, full_name, company, email, password_hash FROM users WHERE email = %s', [email])
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        if not user:
            sql_write("INSERT INTO users (full_name, company, email, password_hash) VALUES (%s, %s, %s, %s)",
            [full_name, company, email, password_hash])

            return render_template('login.html', user_object=user_object)

        elif user:
            error_message = 'That email address already exists.'
            return render_template('signup.html', error_message=error_message, user_object=user_object)
    else:
        error_message = 'That email address is not valid.'
        print("not valid")
        return render_template('signup.html', error_message=error_message, user_object=user_object)

    return redirect('/')

@app.route('/about')
def about():
    user_id = session.get('user_id')
    user_object = login_check(user_id)
    owner_email = session.get('email')

    vineyard_object = vineyard_check(owner_email)

    return render_template('about.html', user_object=user_object, vineyard_object=vineyard_object)

@app.route('/el_stage')
def el():
    user_id = session.get('user_id')
    user_object = login_check(user_id)
    owner_email = session.get('email')

    vineyard_object = vineyard_check(owner_email)

    return render_template('Elstage.html', user_object=user_object, vineyard_object=vineyard_object)

@app.route('/your_vineyard')
def yourvineyard():
    user_id = session.get('user_id')
    user_object = login_check(user_id)
    owner_email = session.get('email')

    vineyard_object = vineyard_check(owner_email)

    return render_template('yourvineyard.html', user_object=user_object, vineyard_object=vineyard_object)

@app.route('/vineyard_confirm', methods=['POST'])
def yourvineyardconfirm():
    user_id = session.get('user_id')
    user_object = login_check(user_id)

    vineyard_site = request.form.get('vineyard_site')
    vineyard_size = request.form.get('vineyard_size')
    varieties = request.form.get('varities')
    elevation  = request.form.get('elevation')
    orientation = request.form.get('orientation')
    E_L_Stage = request.form.get('E_L_Stage')
    owner_email = session.get('email')

    add_vineyard(owner_email, vineyard_site, vineyard_size, varieties, orientation, elevation, E_L_Stage)

    vineyard_object = vineyard_check(owner_email)
    
    return render_template('yourvineyard.html', user_object=user_object, vineyard_object=vineyard_object)

@app.route('/edit_vineyard', methods=['GET'])
def edit_vineyard():
    user_id = session.get('user_id')        
    user_object = login_check(user_id)

    id = request.args.get('id')
    print(id)

    vineyard_object = amend_vineyard(id)

    return render_template('editvineyard.html', vineyard_object=vineyard_object, user_object=user_object, id=id)

@app.route('/save_vineyard', methods=['POST'])
def save_vineyard():
    user_id = session.get('user_id')    
    user_object = login_check(user_id)

    vineyard_site = request.form.get('vineyard_site')
    vineyard_size = request.form.get('vineyard_size')
    varieties = request.form.get('varieties')
    elevation = request.form.get('elevation')
    orientation = request.form.get('orientation')
    E_L_Stage = request.form.get('E_L_Stage')

    id = request.form.get('id')

    if not vineyard_site == "":
        update_vineyard(vineyard_site, vineyard_size, varieties, elevation, orientation, E_L_Stage, id)
        owner_email = session.get('email')
        vineyard_object = vineyard_check(owner_email)
        return render_template('yourvineyard.html', vineyard_object=vineyard_object, user_object=user_object)
    else: 
        return redirect('/')

@app.route('/remove_vineyard', methods=['POST'])
def remove_vineyard():
    id = request.form.get('id')

    delete_vineyard(id)

    return redirect('/')

@app.route('/spray_tool')
def spraytool():
    user_id = session.get('user_id')    
    user_object = login_check(user_id)

    id = request.args.get('id')

    vineyard_object = amend_vineyard(id)

    return render_template('spraytool.html', user_object=user_object, vineyard_object=vineyard_object, id=id)

@app.route('/spray_calculator')
def spray_calculator():
    user_id = session.get('user_id')    
    user_object = login_check(user_id)

    id = request.args.get('id')

    vineyard_object = amend_vineyard(id)
    print(vineyard_object)

    el = vineyard_object['E_L_stage']
    size = vineyard_object['vineyard_size']

    spray_info= check_spray(el)
    print(spray_info)
    
    spray = {
        'vine_stage': spray_info[0],
        'product': spray_info[2],
        'pd_target': spray_info[3],
        'notes': spray_info[4],
        'approx_timing': spray_info[9],
    }

    e_l_record = spray_info[2]
    rate_per_100l = spray_info[7],
    cf = spray_info[8],
    water_rate = spray_info[9],

    if e_l_record == el:
        rate_req_ha = ((rate_per_100l * cf) * water_rate/100)
        print(rate_req_ha)
        chem_req = rate_req_ha * size
        print(chem_req)
    return render_template('spraytool.html', user_object=user_object, vineyard_object=vineyard_object, spray=spray, chem_req=chem_req, rate_req_ha=rate_req_ha)

if __name__ == "__main__":
    app.run(debug=True)
