from flask import *
import sqlite3
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from models.users import User
from models.init import db


class Postes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    context = db.Column(db.String(500), nullable=False)
    img = db.Column(db.String(120), unique=True, nullable=False)
    user_username = db.Column(
        db.Integer,
        db.ForeignKey('user.username', ondelete='CASCADE'),
        nullable=False
        # no need to add index=True, all FKs have indexes
    )
    def __repr__(self):
        return '<Postes %r>' % self.id
