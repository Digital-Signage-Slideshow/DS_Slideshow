from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user

from slideshow.extensions import bcrypt, db
from .forms import RegisterForm, LoginForm
from .models import User

bp = Blueprint('user', __name__, template_folder='templates')


@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('core.setup'))

    if form.validate_on_submit():
        user = User.query.filter_by(id=1).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('core.setup'))
        else:
            flash('Login unsuccessful, please check password')

    return render_template('user/login.html', form=form)


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('core.index'))
