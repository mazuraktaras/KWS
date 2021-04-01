from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from . import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

mail = Mail(app)

# All of these modules should be imported after the application object is created,
# as recommended by the Flask developers.
from kwsapp import views, models, mail

# db.create_all()
