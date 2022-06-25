from slideshow.extensions import db
from slideshow.utils.sql import SQLMixin
from slideshow.utils import generate_random_string


class Display(SQLMixin, db.Model):
    __tablename__ = 'display'
    public_id = db.Column(db.String(10), unique=True, nullable=False)
    location = db.Column(db.String(64))
    active = db.Column(db.Boolean, default=True)

    def deactivate(self):
        self.active = False
        self.save()

    def activate(self):
        self.active = True
        self.save()

    def __init__(self, location="Default"):
        self.public_id = generate_random_string(10)
        self.location = location
        self.active = True
