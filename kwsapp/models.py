from kwsapp import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(512))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


def __repr__(self):
    return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name
