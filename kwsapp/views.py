from . import app, db
from .models import User, Role
from .resources import initial_settings


@app.route('/')
def hello_world():
    initial_settings()
    return f'Hello World!'
