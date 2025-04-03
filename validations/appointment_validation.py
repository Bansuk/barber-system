"""
Validation module for Appointment entities.
"""

from datetime import datetime, timedelta, time
from validations.validation_error import ValidationError
from business.service_business import get_service
from business.employee_business import get_employee
from business.customer_business import get_customer


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
            date (datetime): The appointment date.

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
            date (datetime): The appointment date.

        Returns:
            bool: True if date is in business hours range, False otherwise.
        """

        return AppointmentValidation.OPENING_TIME <= date.time() < AppointmentValidation.CLOSING_TIME

    @staticmethod
    def _are_services_valid(services_ids) -> bool:
        """
        Checks if all provided services ID's exists.

        Returns:
            bool: True if all servicse were found, False otherwise.
        """

        services = {get_service(service_id).id for service_id in services_ids}
        return all(service_id in services for service_id in services_ids)

    @staticmethod
    def _is_employee_valid(employee_id) -> bool:
        """
        Checks if the provided employee exists.

        Returns:
            bool: True if employee was found, False otherwise.
        """

        return get_employee(employee_id) is not None

    @staticmethod
    def _is_customer_valid(customer_id) -> bool:
        """
        Checks if the provided customer exists.

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
            date (datetime): The appointment date.
            employee_id (int): The ID of the employee.
            customer_id (int): The ID of the customer.

        Returns:
            bool: True if there is date is available, False otherwise.
        """
        from business.appointment_business import get_customer_appointment, get_employee_appointment

        return not get_customer_appointment(date, customer_id) and not get_employee_appointment(
            date, employee_id
        )

    @staticmethod
    def _are_inputs_valid(date: datetime, customer_id: int,
                          employee_id: int, services_ids: list[int]) -> bool:
        """
        Validates that all required inputs are provided.

        Args:
            date (datetime): The appointment date.
            customer_id (int): The customer's ID.
            employee_id (int): The employee's ID.
            services_ids (list[int]): List of service IDs.

        Returns:
            bool: True if all inputs are valid, False otherwise.
        """

        return all([date, customer_id, employee_id, services_ids])

    @staticmethod
    def validate_appointment_data(date: datetime, customer_id: int,
                                  employee_id: int, services_ids: list[int]):
        """
        Validates appointment data.

        Args:
            date (datetime): The appointment date.
            customer_id (int): The customer's ID.
            employee_id (int): The employee's ID.
            services_ids (list[int]): List of service IDs.

        Raises:
            ValidationError: If provided email already exists.
        """

        if not AppointmentValidation._are_inputs_valid(date, customer_id,
                                                       employee_id, services_ids):
            raise ValidationError({'input': 'Missing params.'})
        if not AppointmentValidation._is_date_in_valid_range(date):
            raise ValidationError({'date': 'Invalid date.'})
        if not AppointmentValidation._is_time_in_business_hours_range(date):
            raise ValidationError({'date': 'Invalid hour.'})
        if not AppointmentValidation._are_services_valid(services_ids):
            raise ValidationError(
                {'services': 'Provided services were not found.'})
        if not AppointmentValidation._is_employee_valid(employee_id):
            raise ValidationError(
                {'employee': 'Provided employee was not found.'})
        if not AppointmentValidation._is_customer_valid(customer_id):
            raise ValidationError(
                {'customer': 'Provided customer was not found.'})
        if not AppointmentValidation._is_date_available(date, employee_id, customer_id):
            raise ValidationError(
                {'date': 'Date is unavaiable.'})
