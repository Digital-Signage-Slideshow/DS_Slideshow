from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from werkzeug.urls import url_parse

from .forms import RegisterForm, LoginForm, ProfileForm, PasswordForm
from .models import User

bp = Blueprint('user', __name__, template_folder='templates', url_prefix='/user/')


@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})


@bp.get('/login')
def login():
    """
    Render the login page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('core.setup'))
    form = LoginForm()
    return render_template('user/login.html', form=form)


@bp.post('/login')
def login_post():
    """
    Handle the login post request.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('core.setup')
        return redirect(next_page)


@bp.get('/register')
def register():
    """
    Render the register page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('core.setup'))
    form = RegisterForm()
    return render_template('user/register.html', title='Register', form=form)


@bp.post('/register')
def register_post():
    """
    Handle the register post request.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        user.save()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('user.login'))

    if hasattr(form, 'errors'):
        for key, value in form.errors.items():
            flash(value[0], 'warning')
            break


@bp.get('/logout')
@login_required
def logout():
    """
    Handle the logout request.
    """
    logout_user()
    return redirect(url_for('core.index'))


@bp.get('/profile')
@login_required
def profile():
    """
    Render the profile page.
    """
    form = ProfileForm(obj=current_user)
    pwd_form = PasswordForm()
    return render_template('user/profile.html', title='Profile', form=form, pwd_form=pwd_form)


@bp.post('/profile')
@login_required
def profile_post():
    """
    Handle the profile post request.
    """
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.save()
        flash('Your profile has been updated.', 'success')
        return redirect(url_for('user.profile'))

    pwd_form = PasswordForm()
    if pwd_form.validate_on_submit():
        current_user.password = generate_password_hash(pwd_form.new_password.data)
        current_user.save()
        flash('Your password has been updated.', 'success')
        return redirect(url_for('user.profile'))
