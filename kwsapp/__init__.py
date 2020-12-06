from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


# All that modules must be imported after app object created due Flask developers recommendation
from kwsapp import views, models

db.create_all()
