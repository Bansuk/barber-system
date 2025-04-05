"""
Validation module for Appointment entities.
"""

from typing import List
from datetime import datetime, timedelta, time
from flask_smorest import abort
from repositories.employee_repository import get_employee
from repositories.customer_repository import get_customer
from repositories.service_repository import get_service
from repositories.appointment_repository import get_customer_appointment, get_employee_appointment


class AppointmentValidation():
    """
    Validation class for Appointment entities.
    """

    MAX_ADVANCE_DAYS = 7
    OPENING_TIME = time(9, 0)
    CLOSING_TIME = time(18, 0)

    @staticmethod
    def _is_date_in_valid_range(date: datetime) -> bool:
        """
        Validates that the appointment date is in accepted range.

        Args:
            date (datetime): The appointment's date.

        Returns:
            bool: True if appointment date is in valid range, False otherwise.
        """

        now = datetime.now()
        return now <= date <= now + timedelta(days=AppointmentValidation.MAX_ADVANCE_DAYS)

    @staticmethod
    def _is_time_in_business_hours_range(date: datetime) -> bool:
        """
        Validates that the appointment time is in business hours range.

        Args:
            date (datetime): The appointment's date.

        Returns:
            bool: True if date is in business hours range, False otherwise.
        """

        return AppointmentValidation.OPENING_TIME <= date.time() < AppointmentValidation.CLOSING_TIME

    @staticmethod
    def _are_services_valid(services_ids: List[int]) -> bool:
        """
        Checks if all provided services ID's exists.

        Args:
            services_ids (List[int]): List of service IDs.

        Returns:
            bool: True if all servicse were found, False otherwise.
        """

        return all(get_service(service_id) is not None for service_id in services_ids)

    @staticmethod
    def _is_employee_valid(employee_id: int) -> bool:
        """
        Checks if the provided employee exists.

        Args:
            employee_id (int): The employee's ID.

        Returns:
            bool: True if employee was found, False otherwise.
        """

        return get_employee(employee_id) is not None

    @staticmethod
    def _is_customer_valid(customer_id: int) -> bool:
        """
        Checks if the provided customer exists.

        Args:
            customer_id (int): The customer's ID.

        Returns:
            bool: True if customer was found, False otherwise.
        """

        return get_customer(customer_id) is not None

    @staticmethod
    def _is_date_available(date: datetime, employee_id: int, customer_id: int) -> bool:
        """
        Checks if the given appointment time conflicts with any existing appointments
        for the provided customer or employee.

        Args:
            date (datetime): The appointment's date.
            employee_id (int): The ID of the employee.
            customer_id (int): The ID of the customer.

        Returns:
            bool: True if the date is available, False otherwise.
        """

        return not get_customer_appointment(date, customer_id) and not get_employee_appointment(
            date, employee_id
        )

    @staticmethod
    def validate_appointment(date: datetime, customer_id: int,
                             employee_id: int, services_ids: List[int]) -> None:
        """
        Validates appointment.

        Args:
            date (datetime): The appointment's date.
            customer_id (int): The customer's ID.
            employee_id (int): The employee's ID.
            services_ids (List[int]): List of service IDs.

        Raises:
            ValidationError: If any validation fails.
        """

        if not AppointmentValidation._is_date_in_valid_range(date):
            abort(400, message='Invalid date.')

        if not AppointmentValidation._is_time_in_business_hours_range(date):
            abort(400, message='Invalid hour.')

        if not AppointmentValidation._is_date_available(date, employee_id, customer_id):
            abort(409, message='Date is unavailable.')

        if not AppointmentValidation._are_services_valid(services_ids):
            abort(404, message='Provided services were not found.')

        if not AppointmentValidation._is_employee_valid(employee_id):
            abort(404, message='Provided employee was not found.')

        if not AppointmentValidation._is_customer_valid(customer_id):
            abort(404, message='Provided customer was not found.')
