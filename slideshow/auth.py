from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin
import sqlite3

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    if not check_user('Admin'):
        flash('There is no admin password registered...')
        return redirect(url_for('auth.signup'))

    if not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember = remember)
    return redirect(url_for('main.setup'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    password = request.form.get('password')

    if check_user('Admin'):
        flash('There is already an admin login setup')
        return redirect(url_for('auth.login'))

    new_user = create_user(username = name, password = generate_password_hash(password, method='sha256'))

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

def check_user(username : str) -> bool:
    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM account WHERE username = ?', [username])
        return True if cursor.fetchone() else False

def create_user(username : str, password : str):
    with sqlite3.connect(DATABASE_LOGIN) as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO account VALUES(?, ?)', [username, password])