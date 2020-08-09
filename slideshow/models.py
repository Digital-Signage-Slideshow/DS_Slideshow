from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String())

    def __repr__(self):
        return f'{self.id}, {self.username}'


class Content(db.Model):
    path = db.Column(db.String(), primary_key=True)
    priority = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(4))  # img, link, vid

    def __repr__(self):
        return f'{self.path}, {self.priority}'
