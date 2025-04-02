"""
This module defines the Service model for the database.
"""

from datetime import datetime
from database.db_setup import db
from .service_employee import service_employee


class Service(db.Model):
    """
    Represents a service entity in the database.

    Attributes:
        id (int): Primary key identifier.
        name (str): Name of the service.
        price (int): Price of the service.
        employees (list): List of employees that can perform the service.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    employees = db.relationship(
        'Employee', secondary=service_employee, back_populates='services')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price
