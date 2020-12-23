from datetime import datetime
from kwsapp import db
from .models import User, Role
from sqlalchemy.exc import IntegrityError
from faker import Faker


def initial_settings():
    """
        Assets initial DB table's schemas, roles, and fake users
    """
    fake = Faker(['en_GB'])
    db.drop_all()
    db.create_all()
    admin_role = Role(name='admin')
    user_role = Role(name='user')
    guest_role = Role(name='guest')
    inactive_role = Role(name='inactive')
    db.session.add_all([admin_role, user_role, guest_role, inactive_role])
    user = User(name='masurak', email='masurak@ukr.net')
    user.role = admin_role
    user.created_time = datetime.now()
    new_users = []
    for count in range(5):
        print(fake.first_name(), fake.email())
        new_user = User()
        new_user.name = fake.unique.first_name()
        new_user.email = fake.unique.email()
        new_user.role = user_role
        new_user.created_time = datetime.now()
        new_users.append(new_user)
    db.session.add(user)
    db.session.add_all(new_users)
    db.session.commit()


def add_user(name, email, password, role='inactive'):
    try:

        role = Role.query.filter_by(name=role).first()
        new_user = User()
        new_user.name = name
        new_user.email = email
        new_user.password = password
        new_user.role = role
        new_user.created_time = datetime.now()
        db.session.add(new_user)
        db.session.commit()

    except IntegrityError as err:
        print(err.code)
        db.session.rollback()


def users_list():
    users = User.query.all()
    return users


def user_exist(username, email):
    user = User.query.filter_by(name=username).first()
    email = User.query.filter_by(email=email).first()
    if user or email:
        return True
    return False
