import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
gen_key = secrets.token_urlsafe(32)

allowed_extensions = ['png', 'jpg', 'jpeg']
upload_folder = os.path.join(basedir,
                             'slideshow/static/images/slideshow_images')


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', gen_key)

    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_PASS = os.environ.get('DB_PASS')
    DB_USER = os.environ.get('DB_USER')
    DB_NAME = os.environ.get('DB_NAME')
    DB_DIALECT = 'postgresql'
    DB_DRIVER = 'psycopg2'

    @property
    def database_uri(self):
        username = self.DB_USER
        password = self.DB_PASS
        host = self.DB_HOST
        port = self.DB_PORT
        database = self.DB_NAME
        dialict = self.DB_DIALECT
        driver = self.DB_DRIVER
        return '{}+{}://{}:{}@{}:{}/{}'.format(dialict, driver, username,
                                               password, host,
                                               port, database)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = database_uri


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DB_NAME = 'testingdb'


class TestingConfig(Config):
    TESTING = True
