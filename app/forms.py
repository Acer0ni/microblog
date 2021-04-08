from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import data_required

class LoginForm(FlaskForm):
    username = StringField('username',validators=[data_required()])
    password = PasswordField('password', validators=[data_required()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('sign in')