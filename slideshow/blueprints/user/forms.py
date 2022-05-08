from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.validators import EqualTo, ValidationError, InputRequired, Email
from .models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        u = User.query.filter_by(username=username.data).first()

        if u is not None:
            raise ValidationError('a user already exists with that username')

    def validate_email(self, email):
        u = User.query.filter_by(email=email.data).first()

        if u is not None:
            raise ValidationError('a user already exists with that email')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('RememberMe')
    submit = SubmitField('Login')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
