import os
from flask import Flask

from werkzeug.utils import import_string

from .extensions import db, migrate, bcrypt, login_manager
from slideshow.user.models import User

cnf = import_string(
    os.getenv('CONFIG_SETTINGS', 'config.ProductionConfig'))()


def create_app():
    app = Flask(__name__)

    app.config.from_object(cnf)

    from .core.views import bp as core_bp
    from .user.views import bp as user_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(user_bp)

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
    folders = ['images', 'videos', 'images/slideshow_images',
               'videos/slideshow_videos']
    for folder in folders:
        try:
            os.mkdir(f'{current_dir}/static/{folder}', mode=0o755)
        except FileExistsError:
            pass
