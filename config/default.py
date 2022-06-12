"""
********************************************************************************
*                  Default configuration for the application.                  *
********************************************************************************
Do not override this file. use instance/config.py instead.
copy the file to instance/config.py and override the settings you want to change.
to know more about instance/config.py, visit: https://flask.palletsprojects.com/en/2.1.x/config/#instance-folders
"""
import os
from dotenv import load_dotenv

"""
********************************************************************************
Application configuration.
********************************************************************************
"""

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

""" load environment variables from .env file """
load_dotenv(dotenv_path=os.path.join(basedir, '.env'))

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
UPLOAD_FOLDER = os.path.join(basedir, 'slideshow/static/uploads/')

DEBUG = True
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = os.environ['SECRET_KEY']

"""
********************************************************************************
Database configuration.
********************************************************************************
"""
# TODO: add options for different databases
DB_HOST = os.getenv('DB_HOST', 'database')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_USER = os.getenv('DB_USER', 'slideshow')
DB_PASS = os.getenv('DB_PASS', 'password')
DB_NAME = os.getenv('DB_NAME', 'slideshow')
database_uri = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQLALCHEMY_DATABASE_URI = database_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
