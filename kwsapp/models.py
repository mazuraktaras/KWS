from . import db, app
# from .mail import send_email
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha512 as hash512
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Description of records in the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(512), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    created_time = db.Column(db.DateTime)
    email_confirmed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError()

    @password.setter
    def password(self, password):
        self.password_hash = hash512.hash(password)

    def verify_password(self, password) -> bool:
        """
        Takes password and checks if it matches the hash
        :rtype: bool
        """
        if self.password_hash:
            return hash512.verify(password, self.password_hash)

    def generate_email_confirm_token(self):
        serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)
        token = serializer.dumps({'id': self.id})
        return token

    def email_confirm(self, token):
        serializer = Serializer(app.config['SECRET_KEY'])
        try:
            data = serializer.loads(token)
        except BadData:
            return False
        if data['id'] != self.id:
            return False
        self.email_confirmed = True
        self.role_id = 3
        db.session.add(self)
        db.session.commit()
        return True


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
