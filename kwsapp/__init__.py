from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from . import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# All that modules must be imported after app object created due Flask developers recommendation
from kwsapp import views, models

# db.create_all()
