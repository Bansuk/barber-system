"""
Business module for Appointment entities.
"""

from typing import List
from datetime import datetime
from database.db_setup import db
from database.models.appointment import Appointment
from repositories.service_repository import get_service
from validations.appointment_validation import AppointmentValidation


def create_appointment(date: str, customer_id: int,
                       employee_id: int, services_ids: List[int]) -> Appointment:
    """
    Creates a new appointment.

    Args:
        date (str): The appointment's date.
        customer_id (int): The customer's ID.
        employee_id (int): The employee's ID.
        services_ids (List[int]): List of service IDs.

    Returns:
        Appointment: Created appointment.
    """

    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

    AppointmentValidation.validate_appointment(date,
                                               customer_id, employee_id, services_ids)

    services = [get_service(service_id) for service_id in services_ids]

    appointment = Appointment(date, services,
                              employee_id, customer_id)

    try:
        db.session.add(appointment)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        raise error

    return appointment
