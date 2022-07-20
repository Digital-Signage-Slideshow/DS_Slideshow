from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required

from .forms import RegisterForm, LoginForm, EditProfileForm
from .models import User

bp = Blueprint('user', __name__, template_folder='templates', url_prefix='/user/')


@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})


@bp.get('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.setup'))
    form = LoginForm()
    return render_template('user/login.html', form=form)


@bp.post('/login')
def login_post():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('core.setup'))
    return render_template('user/login.html', form=form)


@bp.get('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.setup'))
    form = RegisterForm()
    return render_template('user/register.html', form=form)


@bp.post('/register')
def register_post():
    form = RegisterForm()
    if form.validate_on_submit():
        User(username=form.username.data, email=form.email.data, password=form.password.data).save()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('user.login'))
    return render_template('user/register.html', form=form)


@bp.get('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@bp.get('/profile/')
@login_required
def profile():
    form = EditProfileForm()
    user = User.query.filter_by(id=current_user.id).first()
    form.username.data = user.username
    form.email.data = user.email
    return render_template('user/profile.html', form=form, user=user)


@bp.post('/profile/')
@login_required
def profile_post():
    form = EditProfileForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = form.password.data
        user.update()
        flash('Your changes have been saved.')
        return redirect(url_for('user.profile'))
    return render_template('user/profile.html', form=form)
