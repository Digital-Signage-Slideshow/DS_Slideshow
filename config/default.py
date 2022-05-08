"""
********************************************************************************
*                  Default configuration for the application.                  *
********************************************************************************
Do not override this file. use instance/config.py instead. to override
"""
import os
from dotenv import load_dotenv

"""
********************************************************************************
Application configuration.
********************************************************************************
"""

""" load environment variables from .env file """
load_dotenv()

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

allowed_extensions = ['png', 'jpg', 'jpeg']
upload_folder = os.path.join(basedir, 'slideshow/static/images/slideshow_images')

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