"""
This module defines the Service model for the database.
"""

from typing import TYPE_CHECKING
from datetime import datetime
from database.db_setup import db
from .service_appointment import service_appointment
from .service_employee import service_employee

if TYPE_CHECKING:
    from database.models.appointment import Appointment
    from database.models.employee import Employee


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
    appointments = db.relationship(
        'Appointment', secondary=service_appointment, back_populates='services')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name: str, price: int,
                 employees: list['Employee'], appointments: list['Appointment']) -> None:
        self.name = name
        self.price = price
        self.employees = employees
        self.appointments = appointments

    def to_dict(self):
        """
        Converts the Service instance into a dictionary format.

        Returns:
            dict: A dictionary containing service details and associated employees and appointments.
        """

        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "employees": [employee.id for employee in self.employees],
            "appointments": [appointment.id for appointment in self.appointments]
        }
