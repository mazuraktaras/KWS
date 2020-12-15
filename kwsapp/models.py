from kwsapp import db
from passlib.hash import pbkdf2_sha512 as hash512


class User(db.Model):
    __tablename__ = 'users'

    # Description of records in the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(512), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError()

    @password.setter
    def password(self, password):
        self.password_hash = hash512.hash(password)


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

# class Post(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(255))
#     text = db.Column(db.Text())
#     publish_date = db.Column(db.DateTime())
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return "<Post '{}'>".format(self.title)


# class User(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(255))
#     password = db.Column(db.String(255))
#     posts = db.relationship(
#         'Post',
#         backref='user',
#         lazy='dynamic'
#     )
