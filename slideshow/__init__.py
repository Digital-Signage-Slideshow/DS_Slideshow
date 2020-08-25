from os import mkdir
from os.path import exists, abspath, dirname
from flask import Flask

from .extensions import db, migrate, bcrypt, login_manager


def create_default_folders():
    current_dir = dirname(abspath(__file__))

    for folder in ('slideshow_images', 'slideshow_videos'):
        if not exists(f'{current_dir}/static/images/{folder}'):
            mkdir(f'{current_dir}/static/images/{folder}')

def create_app():
    app = Flask(__name__)

    create_default_folders()

    app.config.from_object('config.DevelopmentConfig')
 
    from .core.views import bp as core_bp
    from .user.views import bp as user_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(user_bp)

    extensions(app)

    with app.app_context():
        db.create_all()

    return app


def extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)