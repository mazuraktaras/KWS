from flask import Flask

app = Flask(__name__)

# All that modules must be imported after app object created due Flask developers recommendation
from kwsapp import views