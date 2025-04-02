"""
Business module for Appointment entities.
"""
from typing import List
from datetime import datetime
from business.service_business import get_service
from database.models.appointment import Appointment
from database.db_setup import db
from validations.appointment_validation import AppointmentValidation


def create_appointment(date: datetime, customer_id: int,
                       employee_id: int, services_ids: list[int]) -> Appointment:
    """
    Business class for creating a new Appointment.

    Args:
        date (datetime): The appointment date.
        customer_id (int): The customer's ID.
        employee_id (int): The employee's ID.
        services_ids (list[int]): List of service IDs.

    Returns:
        Appointment: Created appointment.
    """

    AppointmentValidation.validate_appointment_data(date,
                                                    customer_id, employee_id, services_ids)

    services = []
    for service_id in services_ids:
        service = get_service(service_id)
        services.append(service)

    appointment = Appointment(date, services,
                              employee_id, customer_id)
    db.session.add(appointment)
    db.session.commit()

    return appointment


def get_appointments() -> List[Appointment]:
    """
    Business class for getting all 
     registered Appointments.

    Returns:
        List[Appointment]: A List of registered appointments.
    """

    return db.session.query(Appointment).all()


def get_appointments_count() -> int:
    """
    Business class for getting the number
     of registered Appointments.

    Returns:
        int: The number of registered appointments.
    """

    return db.session.query(Appointment).count()


def get_appointment(appointment_id) -> Appointment:
    """
    Business class for getting a Appointment by its id.

    Returns:
        Appointment: The appointment found.
    """

    return db.session.query(Appointment).filter_by(id=appointment_id).first()
