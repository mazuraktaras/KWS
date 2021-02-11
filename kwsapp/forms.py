from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    """
    Describes the user credentials form in the frontend for signup and login
    """
    username = StringField('Username', validators=[DataRequired(), Length(max=128)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    # submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """
    Describes the form of user credentials in the frontend for login
    """
    # username = StringField('Username', validators=[DataRequired(), Length(max=128)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    # submit = SubmitField('Register')
