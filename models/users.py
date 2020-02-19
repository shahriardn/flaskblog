from flask import *
import sqlite3
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from models.init import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    postes = db.relationship('Postes', backref='user', lazy=True)
        
    def __repr__(self):
        return '<User %r>' % self.username
