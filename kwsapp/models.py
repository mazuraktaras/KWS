from kwsapp import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(512))

    def __repr__(self):
        return '<User %r>' % self.username


