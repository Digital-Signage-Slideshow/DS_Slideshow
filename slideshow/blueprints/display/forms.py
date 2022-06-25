from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired


class DisplayForm(FlaskForm):
    """
    Form for creating a new display.
    """
    location = StringField('Location', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Create')


class EditDisplayForm(FlaskForm):
    """
    Form for editing a display.
    """
    location = StringField('Location', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    active = BooleanField('Active')
    submit = SubmitField('Update')
