from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()

Session = sessionmaker(bind=db)
session = Session()

login_manager = LoginManager()
login_manager.login_view = 'user.login'

bcrypt = Bcrypt()
