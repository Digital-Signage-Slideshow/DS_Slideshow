from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from slideshow.utils import slugify_text

from slideshow.extensions import db
from slideshow.utils.sql import SQLMixin


class User(SQLMixin, UserMixin, db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(50), unique=True, nullable=False)
    slug = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String())
    active = db.Column(db.Boolean, default=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def __init__(self, username, email, password):
        self.username = username
        self.slug = slugify_text(username)
        self.email = email
        self.password = generate_password_hash(password)
