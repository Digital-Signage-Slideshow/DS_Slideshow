from flask import Blueprint, render_template

bp = Blueprint('user', __name__, template_folder='templates')


@bp.route('/login')
def login():
    return render_template('user/login.html', title='Login')
