import os
from flask import Flask

from .extensions import db, migrate, bcrypt, login_manager
from slideshow.user.models import User
from .utils import create_directory


def create_app(config_class=None):
    """
    Create and configure an instance of the Flask application.

    Args:
        config_class: str: name of the config class to use. defaults to ProductionConfig

    Returns:
        app: Flask: the Flask application
    """
    if config_class is None:
        config_class = 'config.ProductionConfig'

    app = Flask(__name__)

    app.config.from_object(config_class)

    @app.before_first_request
    def before_first_request():
        """
        Before the first request, create the directories and database for the application.
        """
        # Create the directories
        create_directories()

        # Create the database
        db.create_all()

    from .core.views import bp as core_bp
    from .user.views import bp as user_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(user_bp)

    extensions(app)

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
    """
    Create the directories for the application.
    """
    # Create the upload directory
    try:
        create_directory(os.getcwd(), 'uploads')
    except FileExistsError:
        pass

    # Create the images/video directory
    try:
        folders = ['images', 'videos']
        for folder in folders:
            create_directory(os.path.join(os.getcwd(), 'uploads'), folder)
    except FileExistsError:
        pass
