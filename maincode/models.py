from maincode import db, login_manager
from flask import current_app as app
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(20), unique=True, nullable=False)
    ELO =db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.instatag}', '{self.ELO}' )"
