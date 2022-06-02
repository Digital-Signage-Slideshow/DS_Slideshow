from datetime import datetime

from slideshow.extensions import db


class SQLMixin:
    """
    Adds the ability to save and delete row's from database by passing a .save() .update() or .delete()
    example: user = User(username='test').save() or user.update(username='test') or user.delete()
    """

    # adds created_on and updated_on to model
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def save(self):
        """
        Save the model instance
        return: model instance
        """
        db.session.add(self)
        db.session.commit()

        return self

    def update(self, **kwargs):
        """
        Update the model instance
        return: model instance
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

        return self

    def delete(self):
        """
        Delete the model instance
        return: commit session result
        """
        db.session.delete(self)
        return db.session.commit()
