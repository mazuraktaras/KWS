from kwsapp import app, db
from kwsapp.models import User, Role

db.create_all()


def initial_settings():

    admin_role = Role(name='admin')
    user_role = Role(name='user')
    guest_role = Role(name='guest')
    inactive_role = Role(name='inactive')
    db.session.add_all([admin_role, user_role, guest_role, inactive_role])
    user = User(name='new@email.com')
    user.role = user_role
    db.session.add(user)
    db.session.commit()

user = User()
user.name = 'test'