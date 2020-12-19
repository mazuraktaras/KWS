from kwsapp import db
from passlib.hash import pbkdf2_sha512 as hash512


class User(db.Model):
    __tablename__ = 'users'

    # Description of records in the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(512), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    created_time = db.Column(db.DateTime)

    @property
    def password(self):
        raise AttributeError()

    @password.setter
    def password(self, password):
        self.password_hash = hash512.hash(password)

    def verify_password(self, password):
        """
        Takes password and checks if it matches the hash
        :rtype: bool
        """
        return hash512.verify(password, self.password)


def __repr__(self):
    # return '<User %r>' % self.name
    return f'User {self.name!r}'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

