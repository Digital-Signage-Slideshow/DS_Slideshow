from slideshow.extensions import db


class Content(db.Model):
    path = db.Column(db.String(), primary_key=True)
    priority = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(4))  # img, link, vid

    def __repr__(self):
        return f'{self.path}, {self.priority}'
