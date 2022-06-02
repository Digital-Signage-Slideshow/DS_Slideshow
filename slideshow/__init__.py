import os
from flask import Flask

from .extensions import db, migrate, bcrypt, login_manager
from slideshow.blueprints.user.models import User

from .blueprints import all_blueprints


def create_app():
    """
    Create and configure an instance of the Flask application.
    return: Flask application instance
    """
    app = Flask(__name__, instance_relative_config=True)

    """Load the default config file."""
    app.config.from_object('config.default')
    """Load the instance config file."""
    app.config.from_pyfile('config_old.py', silent=True)

    for blueprint in all_blueprints:
        app.register_blueprint(blueprint)

    extensions(app)

    with app.app_context():
        db.create_all()
        create_directories()

    return app


def extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))


def create_directories():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    folders = ['images', 'videos']
    for folder in folders:
        try:
            os.mkdir(f'{current_dir}/static/uploads/{folder}', mode=0o666)
        except FileExistsError:
            pass
