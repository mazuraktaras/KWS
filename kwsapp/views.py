from . import app, db
from .models import User

@app.route('/')
def hello_world():
    new_user = User(name='newIm')
    db.session.add(new_user)
    db.session.commit()
    return 'Hello World!'
