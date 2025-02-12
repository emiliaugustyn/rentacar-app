from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from rentacar.models import *


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password',
                                                                             message='Passwords must match!')])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    pesel = StringField('Pesel', validators=[DataRequired(), Length(min=11, max=11)])
    phone_number = StringField('Phone number', validators=[DataRequired(), Length(min=9, max=9)])
    id_number = StringField('Id number', validators=[DataRequired(), Length(min=9, max=9)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        client = session.query(Client).filter_by(username=username.data).first()
        if client:
            raise ValidationError('That username is taken!')

    def validate_email(self, email):
        client = session.query(Client).filter_by(email=email.data).first()
        if client:
            raise ValidationError('That account already exists!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
