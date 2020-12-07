from kwsapp import app, db
from kwsapp.models import User, Role

@app.shell_context_processor
def make_hell_context():
    return dict(app=app, db=db, User=User, Role=Role)
