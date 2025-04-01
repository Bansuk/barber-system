"""
Setup module for the database.
"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from database.config import DATABASE_URI

db = SQLAlchemy()


def init_db(app: Flask):
    """
    Initialize database.

    Args:
        app (Flask): The Flask application instance.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
