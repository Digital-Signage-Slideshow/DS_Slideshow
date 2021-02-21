from datetime import datetime

from slideshow.extensions import db


class DSMixin(object):
    """
    Digital Signage Slider custom mixin
    adds timestamps to models & the ability to save and delete row's from database by passing a .save() or .delete()
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

    def delete(self):
        """
        Delete the model instance
        return: commit session result
        """
        db.session.delete(self)
        return db.session.commit()
