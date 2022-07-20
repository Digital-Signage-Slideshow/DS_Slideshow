from slideshow.extensions import db


class Content(db.Model):
    path = db.Column(db.String(), primary_key=True)
    priority = db.Column(db.Integer(), default=0)
    type = db.Column(db.String(4))  # img, link, vid
    interval = db.Column(db.Integer(), default=1000)  # in milliseconds
    active = db.Column(db.Boolean, default=True)

    def update_priority(self):
        self.priority = Content.query.count() + 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_priority()
        self.path = kwargs['path']
        self.type = kwargs['type']

    def __repr__(self):
        return f'{self.path}, {self.priority}'
