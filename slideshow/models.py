from slideshow import database

class User(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String(25), unique = True, nullable = False)
    password = database.Column(database.String())

    def __repr__(self):
        return f'{self.id}, {self.username}'

class Content(database.Model):
    path = database.Column(database.String(), primary_key = True)
    priority = database.Column(database.Integer, unique = True, autoincrement = True)
    type = database.Column(database.String(4)) # img, link, vid

    def __repr__(self):
        return f'{self.path}, {self.priority}'