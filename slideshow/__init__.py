from os import mkdir
from os.path import exists, abspath, dirname
from flask import Flask

from .extensions import db, migrate, bcrypt, login_manager
from slideshow.user.models import User

def create_default_folders():
    current_dir = dirname(abspath(__file__))

    for folder in ('slideshow_images', 'slideshow_videos'):
        if not exists(f'{current_dir}/static/images/{folder}'):
            mkdir(f'{current_dir}/static/images/{folder}')


def init_default_login():
    accounts = User.query.all()

    if not accounts:
        # generate the default password hash
        default_password = 'password'
        hashed_password = bcrypt.generate_password_hash(default_password).decode('utf-8')

        default_account = User(id = 1, username = 'default', password = hashed_password)
        db.session.add(default_account)
        db.session.commit()


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
        init_default_login()

    return app


def extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)