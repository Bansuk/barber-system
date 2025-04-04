"""
This module defines the Employee model for the database.
"""
from typing import TYPE_CHECKING
from datetime import datetime
from database.db_setup import db
from .service_employee import service_employee

if TYPE_CHECKING:
    from .service import Service
    from .appointment import Appointment


class Employee(db.Model):
    """
    Represents a employee entity in the database.

    Attributes:
        id (int): Primary key identifier.
        name (str): Name of the employee.
        email (str): Unique email of the employee.
        services (list): List of services that the employee can perform.
        appointments (list): List of appointments assigned to the employee.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    services = db.relationship(
        'Service', secondary=service_employee, back_populates='employees')
    appointments = db.relationship(
        'Appointment', back_populates='employees')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name: str, email: str, services: list['Service'],
                 appointments: list['Appointment']) -> None:
        self.name = name
        self.email = email
        self.services = services
        self.appointments = appointments

    def to_dict(self):
        """
        Converts the Emplyee instance into a dictionary format.

        Returns:
            dict: A dictionary containing employee details and associated appointments.
        """

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "services": [service.id for service in self.services],
            "appointments": [appointment.id for appointment in self.appointments]
        }
