from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

# All that modules must be imported after app object created due Flask developers recommendation
from kwsapp import views
