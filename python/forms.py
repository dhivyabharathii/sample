from flask_wtf import FlaskForm
from wtforms import Form,validators

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(Form):
    username = StringField('Username',
                           validators=[validators.InputRequired(), validators.Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[validators.InputRequired(), Email()])
    password = PasswordField('Password', validators=[validators.InputRequired(),validators.Length(min=2, max=20)])
    

class LoginForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
