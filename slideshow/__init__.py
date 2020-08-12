from flask import Flask

from .extensions import db, migrate, bcrypt, login_manager
# from slideshow.user.models import User


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

    from .core.views import bp as core_bp
    from .user.views import bp as user_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(user_bp)

    extensions(app)

    # authentication(app, User)

    with app.app_context():
        db.create_all()

    return app


def extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)


# def authentication(app, user_model):
#     login_manager.login_view = 'user.login'
#
#     @login_manager.user_loader
#     def load_user(user_id: str) -> User:
#         # should always return 1 until other users are supported
#         return User.query.get(int(user_id))

