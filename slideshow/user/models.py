from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from slideshow.extensions import db
from slideshow.utils.sql import DSMixin


class User(DSMixin, UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String())
    active = db.Column(db.Boolean, default=True)

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)
