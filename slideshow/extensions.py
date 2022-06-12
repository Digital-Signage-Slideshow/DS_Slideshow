from flask_sqlalchemy import Model, SQLAlchemy
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


class IdModel(Model):
    """
    Base model class that includes an auto-incrementing primary key.
    """

    @declared_attr
    def id(cls):
        for base in cls.__mro__[1:-1]:
            if getattr(base, '__table__', None) is not None:
                col_type = sa.ForeignKey(base.id, ondelete='CASCADE')
                break
        else:
            col_type = sa.Integer()
        return sa.Column(col_type, primary_key=True)


db = SQLAlchemy(model_class=IdModel)
migrate = Migrate()

Session = sessionmaker(bind=db)
session = Session()

login_manager = LoginManager()
login_manager.login_view = 'user.login'

bcrypt = Bcrypt()
