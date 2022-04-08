from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, InputRequired
from cycle.models import User

csrf = CSRFProtect()

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password1 = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField(label='Sign in')



class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Name cannot be empty')])
    email = StringField('E-mail', validators=[DataRequired('Email cannot be empty'),Email('Enter a valid email')])
    subject = StringField('Subject', validators=[DataRequired('Subject cannot be empty')])
    message = TextAreaField('Message', validators=[DataRequired('Message cannot be empty')])
    submit = SubmitField("Submit")

