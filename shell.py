from kwsapp import app, db
from kwsapp.models import User, Role

users = User.query.all()


