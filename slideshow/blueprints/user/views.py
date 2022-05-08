from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

from .forms import RegisterForm, LoginForm, EditProfileForm, ChangePasswordForm
from .models import User

bp = Blueprint('user', __name__, template_folder='templates', url_prefix='/user/')


@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('username or password incorrect', 'danger')
            return redirect(url_for('.login'))

        login_user(user, remember=form.remember.data)
        return redirect(url_for('core.setup'))

    return render_template('user/login.html', title='Login', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        u = User(username=form.username.data, email=form.email.data, password=form.password.data)
        u.save()
        return redirect(url_for('user.login'))
    else:
        if hasattr(form, 'errors'):
            for key, value in form.errors.items():
                flash(value[0], 'warning')
                break

    return render_template('user/register.html', form=form)


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('core.index'))


@bp.route('/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EditProfileForm(obj=user)
    cpform = ChangePasswordForm()

    if form.validate_on_submit():
        form.populate_obj(user)
        user.update()
        flash('Your changes have been saved..', 'success')
        return redirect(url_for('.profile', username=current_user.username))

    if cpform.validate_on_submit():
        if user.check_password(cpform.old_password.data):
            User.password = generate_password_hash(cpform.new_password.data)
            user.update()
            flash('Your password has been changed.', 'success')
            return redirect(url_for('.profile', username=current_user.username))
    return render_template('user/profile.html', title='Profile', user=user, form=form, cpform=cpform)
