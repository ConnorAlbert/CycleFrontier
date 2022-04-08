from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os
from os import environ






app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cycle.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

mail_settings = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USERNAME': os.environ['MAIL_USERNAME'],
    'MAIL_PASSWORD': os.environ['MAIL_PASSWORD'],
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True
}
app.config.update(mail_settings)
mail = Mail(app)


from cycle import routes