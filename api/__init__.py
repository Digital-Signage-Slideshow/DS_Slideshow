import os

from flask import Flask

from .extensions import db, migrate, bcrypt, jwt, session
from .user.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    from .core.routes import blueprint as core_bp
    from .user.routes import blueprint as user_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(user_bp)

    register_extensions(app)

    with app.app_context():
        db.create_all()
        create_directories()

        username=app.config['DEFAULT_USERNAME']
        email=app.config['DEFAULT_EMAIL']
        password=app.config['DEFAULT_PASSWORD']

        default_user = User.query.filter_by(username=username).first()
        if not default_user:
            default = User(
                username=username, 
                email=email
            )
            default.hash_password(password)
            default.save()

    return app

def register_extensions(app):
    db.init_app(app)

    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

def create_directories():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    folders = ['images', 'videos']
    for folder in folders:
        try:
            os.mkdir(f'{current_dir}/static/{folder}', mode=0o666)
        except FileExistsError:
            pass
