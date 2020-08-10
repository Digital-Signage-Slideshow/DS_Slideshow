from flask import Blueprint, render_template

bp = Blueprint('user', __name__, template_folder='templates')

@bp.route('/register')
def register():
    form = Register()
    return render_template('register.html', form = form)

@bp.route('/login')
def login():
    form = Login()
    return render_template('login.html', form = form)