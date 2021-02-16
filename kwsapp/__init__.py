from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from . import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)


# All of these modules should be imported after the application object is created,
# as recommended by the Flask developers.
from kwsapp import views, models

# db.create_all()
