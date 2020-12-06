from . import app, db
from .models import User

@app.route('/')
def hello_world():
    new_user = User(username='newIm')
    print(repr(new_user))
    db.session.add(new_user)
    db.session.commit()
    return 'Hello World!'
