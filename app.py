from database import sql_select, sql_write
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
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT 1', []) # Query to check that the DB connected
    conn.close()
    return render_template('base.html')

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

    user_info = sql_select("SELECT id, name, email, password_hash FROM users WHERE email = %s", [email])
    print(user_info)

    password_hash = user_info[0][3]
    print(password_hash)
    print(password)

    valid = bcrypt.checkpw(password.encode(), password_hash.encode())
    print(valid)
    
    if len(user_info) == 0:
        return redirect('/login')
    elif valid:
        session['user_email'] = user_info[0][1]
        session['username'] = user_info[0][2]
        session['user_id'] = user_info[0][0]
        session['password_hash'] = user_info[0][3]
        return redirect('/')
    else:
        return redirect('/login') 

if __name__ == "__main__":
    app.run(debug=True)
