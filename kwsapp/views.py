from . import app, db
from .models import User, Role


@app.route('/')
def hello_world():
    return f'Hello World!'
