import os

basedir = os.path.abspath(os.path.dirname(__file__))

allowed_extensions = ['png', 'jpg', 'jpeg']
upload_folder = os.path.join(basedir, 'slideshow/static/images/slideshow_images')


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Database configuration defaults to PostgreSQL
    DB_TYPE = os.getenv('DB_TYPE', 'postgresql')
    DB_USER = os.getenv('DB_USER', 'slideshow')
    DB_PASS = os.getenv('DB_PASS', 'password')
    DB_HOST = os.getenv('DB_HOST', 'database')
    DB_NAME = os.getenv('DB_NAME', 'slideshow')
    DB_PORT = os.getenv('DB_PORT', '5432')
    SQLALCHEMY_DATABASE_URI = f'{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'slideshow.db')


class TestingConfig(Config):
    TESTING = True
