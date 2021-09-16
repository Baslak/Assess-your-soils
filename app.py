from database import sql_select, sql_write
from models.users import login_check

from flask import Flask, request, render_template, redirect, session

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

    return render_template('base.html', user_object=user_object)

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

    user_info = sql_select("SELECT id, full_name, company, email, password_hash FROM users WHERE email = %s", [email])
    print(user_info)

    password_hash = user_info[0][4]
    print(password_hash)
    print(password)

    valid = bcrypt.checkpw(password.encode(), password_hash.encode())
    print(valid)
    
    if len(user_info) == 0:
        return redirect('/login')
    elif valid:
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

    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    user = sql_select('SELECT id, full_name, company, email, password_hash FROM users WHERE email = %s', [email])

    if not user:
        sql_write("INSERT INTO users (full_name, company, email, password_hash) VALUES (%s, %s, %s, %s)",
        [full_name, company, email, password_hash])
    else:
        error_message = 'That email address already exists. Please try again.'
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
    
    return render_template('yourvineyard.html')

@app.route('/spray_tool')
def spraytool():
    
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
