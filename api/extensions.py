from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

Session = sessionmaker(bind=db)
session = Session()

bcrypt = Bcrypt()
