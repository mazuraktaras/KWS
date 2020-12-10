from kwsapp import db
from kwsapp.models import User, Role


def initial_settings():
    db.drop_all()
    db.create_all()
    admin_role = Role(name='admin')
    user_role = Role(name='user')
    guest_role = Role(name='guest')
    inactive_role = Role(name='inactive')
    db.session.add_all([admin_role, user_role, guest_role, inactive_role])
    user = User(name='masurak@ukr.net')
    user.role = user_role
    db.session.add(user)
    db.session.commit()
