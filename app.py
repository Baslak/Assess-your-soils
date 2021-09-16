from re import template
from database import sql_select, sql_write
from models.users import login_check
from models.vineyards import add_vineyard, vineyard_check, delete_vineyard, update_vineyard

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
    print(user_id)
    user_object = login_check(user_id)

    return render_template('base.html', user_id=user_id, user_object=user_object)

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/login_confirm', methods=['POST'])
def login_confirm():
    email = request.form.get('email')
    password = request.form.get('password')
    print(password)

    user_info = sql_select("SELECT id, full_name, company, email, password_hash FROM users WHERE email = %s", [email])
    
    if email == "" or len(user_info) == 0:
        no_strings_attached = 'No dice, i need strings!'
        return render_template('login.html', no_strings_attached=no_strings_attached)
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

    return render_template('signup.html')

@app.route('/signup_action', methods=['POST'])
def signup_action():
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

        elif user:
            error_message = 'That email address already exists. Please try again.'
            return render_template('signup.html', error_message=error_message)
    else:
        error_message = 'That email address is not valid. Please try again.'
        print("not valid")
        return render_template('signup.html', error_message=error_message)

    return redirect('/')

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/contact')
def contact():
    
    return render_template('contact.html')

@app.route('/your_vineyard')
def yourvineyard():
    user_id = session.get('user_id')
    user_object = login_check(user_id)
    owner_email = session.get('email')
    print(owner_email)

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
    owner_email = session.get('email')
    print(owner_email)
    print(vineyard_site)

    add_vineyard(owner_email, vineyard_site, vineyard_size, varieties, orientation, elevation)

    vineyard_object = vineyard_check(owner_email)

    return render_template('yourvineyard.html', user_object=user_object, vineyard_object=vineyard_object)

@app.route('/edit_vineyard', methods=['POST'])
def edit_vineyard():
    id = request.form.get('id')
    
    vineyard_site = request.form.get('vineyard_site')
    print(vineyard_site)
    vineyard_size = request.form.get('vineyard_size')
    varieties = request.form.get('varieties')
    elevation = request.form.get('elevation')
    orientation = request.form.get('orientation')

    update_vineyard(vineyard_site, vineyard_size, varieties, orientation, elevation, id)

    return render_template('/your_vineyard')

@app.route('/delete_vineyard', methods=['POST'])
def delete_vineyard():
    id = request.form.get('id')

    delete_vineyard(id)

    return redirect('/')

@app.route('/spray_tool')
def spraytool():
    
    return render_template('spraytool.html')

if __name__ == "__main__":
    app.run(debug=True)
