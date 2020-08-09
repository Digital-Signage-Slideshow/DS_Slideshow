from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from .models import User

class Register(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Add Password')

    def validate_password(self, password):
        user = User.query.filter_by(username = 'Admin').first()

        if user:
            print('validation error raised')
            raise ValidationError('An admin password has already been set')

class Login(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('RememberMe')
    submit = SubmitField('Login')