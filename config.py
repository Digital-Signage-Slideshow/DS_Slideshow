import os

basedir = os.path.abspath(os.path.dirname(__file__))

allowed_extensions = ['png', 'jpg', 'jpeg']
upload_folder = os.path.join(basedir, 'slideshow/static/images/slideshow_images')


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://slideshow_user:password@localhost:5432/slideshow'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.urandom(24)

    DEFAULT_USERNAME='admin'
    DEFAULT_EMAIL='admin'
    DEFAULT_PASSWORD='password'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True