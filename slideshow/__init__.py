from flask import Flask

from .extensions import db, migrate, bcrypt, login_manager
from .config import DevelopmentConfig

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    from .routes import bp as core_bp

    app.register_blueprint(core_bp)

    extensions(app)

    with app.app_context():
        db.create_all()

    return app

def extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)