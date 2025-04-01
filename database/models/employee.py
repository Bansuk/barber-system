"""
This module defines the Employee model for the database.
"""

from datetime import datetime
from database.db_setup import db


class Employee(db.Model):
    """
    Represents a employee entity in the database.

    Attributes:
        id (int): Primary key identifier.
        name (str): Name of the employee.
        email (str): Unique email of the employee.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    picture = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
