from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
migrate = Migrate()

Session = sessionmaker(bind = db)
session = Session()

login_manager = LoginManager()
login_manager.login_view = 'core.login'

bcrypt = Bcrypt()