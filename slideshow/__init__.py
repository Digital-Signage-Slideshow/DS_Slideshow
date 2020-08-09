from flask import Flask
from slideshow.auth import auth

from .extensions import db, migrate
from .config import DevelopmentConfig


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    from .routes import bp as core_bp

    app.register_blueprint(core_bp)

    extensions(app)

    return app


def extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)
    return None


def authentication(app, user_model):
    # login_manager.login_view = 'user.login'
    pass

# database.create_all()

# app.register_blueprint(auth)
# app.secret_key = os.urandom(24)
