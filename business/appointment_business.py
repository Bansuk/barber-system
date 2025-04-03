"""
Business module for Appointment entities.
"""
from typing import List, Optional
from datetime import datetime
from business.service_business import get_service
from database.models.appointment import Appointment
from database.db_setup import db
from validations.appointment_validation import AppointmentValidation


def create_appointment(date: str, customer_id: int,
                       employee_id: int, services_ids: list[int]) -> Appointment:
    """
    Creates a new appointment.

    Args:
        date (datetime): The appointment date.
        customer_id (int): The customer's ID.
        employee_id (int): The employee's ID.
        services_ids (list[int]): List of service IDs.

    Returns:
        Appointment: Created appointment.
    """

    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

    AppointmentValidation.validate_appointment_data(date,
                                                    customer_id, employee_id, services_ids)

    services = [get_service(service_id) for service_id in services_ids]

    appointment = Appointment(date, services,
                              employee_id, customer_id)
    db.session.add(appointment)
    db.session.commit()

    return appointment


def get_appointments() -> List[Appointment]:
    """
    Retrieves all registered appointments.

    Returns:
        List[Appointment]: A list of registered appointments.
    """

    return db.session.query(Appointment).all()


def get_appointments_count() -> int:
    """
    Retrieves the number of registered appointments.

    Returns:
        int: The total number of appointments.
    """

    return db.session.query(Appointment).count()


def get_appointment(appointment_id: int) -> Optional[Appointment]:
    """
    Retrieves an appointment by its ID.

    Args:
        appointment_id (int): The appointment ID.

    Returns:
         Optional[Appointment]: The appointment found or None.
    """

    return db.session.query(Appointment).filter_by(id=appointment_id).first()


def get_customer_appointment(date: datetime, customer_id: int) -> Optional[Appointment]:
    """
    Retrieves a customer appointment by date.

    Args:
        date (datetime): The appointment date.
        customer_id (int): The customer's ID.

    Returns:
         Optional[Appointment]: The appointment found or None.
    """

    return db.session.query(Appointment).filter(
        Appointment.customer_id == customer_id,
        Appointment.date == date
    ).first()


def get_employee_appointment(date: datetime, employee_id: int) -> Optional[Appointment]:
    """
    Retrieves an employee appointment by date.

    Args:
        date (datetime): The appointment date.
        employee_id (int): The employee's ID.

    Returns:
         Optional[Appointment]: The appointment found or None.
    """

    return db.session.query(Appointment).filter(
        Appointment.employee_id == employee_id,
        Appointment.date == date
    ).first()
