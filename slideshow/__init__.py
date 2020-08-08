from flask import Flask
import os
# from flask_login import login_user, logout_user, login_required, LoginManager
from slideshow.auth import auth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this_key_is_very_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slideshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
# database.create_all()

# app.register_blueprint(auth)
# app.secret_key = os.urandom(24)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

from slideshow import routes