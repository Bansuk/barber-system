"""
This module defines the Customer model for the database.
"""

from datetime import datetime, timezone
from database.db_setup import db


class Customer(db.Model):
    """
    Represents a customer entity in the database.

    Attributes:
        id (int): Primary key identifier.
        name (str): Name of the customer.
        email (str): Unique email of the customer.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """

    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    appointments = db.relationship(
        'Appointment', back_populates='customer', cascade='all, delete-orphan')
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
