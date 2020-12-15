from kwsapp import db
from .models import User, Role
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
    new_users = []
    for count in range(10):
        print(fake.first_name(), fake.email())
        new_user = User()
        new_user.name = fake.unique.first_name()
        new_user.email = fake.unique.email()
        new_user.role = user_role
        new_users.append(new_user)
    db.session.add(user)
    db.session.add_all(new_users)
    db.session.commit()


# role = Role.query.filter_by(name=role).first()

def add_user(name, password, role='user'):

    role = Role.query.filter_by(name=role).first()
    new_user = User(name=name, role=role)
    new_user.password = password

    return

def users_list():
    users = User.query.all()
    # print(users)
    return users
