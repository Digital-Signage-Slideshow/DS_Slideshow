from dataclasses import dataclass

from api.extensions import db

@dataclass
class Content(db.Model):
    path: str
    priority: int
    rotation_speed: int
    type: str

    path = db.Column(db.String(), primary_key=True)
    priority = db.Column(db.Integer, unique=True) # The order of the slides
    rotation_speed = db.Column(db.Integer, nullable=False, default=30) # How long the slide stays up in seconds
    type = db.Column(db.String(4)) # img, link, vid

    def __repr__(self):
        return f'<Slide: {self.priority}>'