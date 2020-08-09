from flask_login import UserMixin


class User(UserMixin):
    def is_active(self):
        return True

    def get_id(self, username: str = 'Admin'):
        with sqlite3.connect(DATABASE_LOGIN) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT id FROM account WHERE username = ?',
                           [username])

            return cursor.fetchone()[0]

    def is_authenticated(self):
        with sqlite3.connect(DATABASE_LOGIN) as connection:
            cursor = connection.cursor()
            cursor.execute()

    def is_anonymous(self):
        return False
