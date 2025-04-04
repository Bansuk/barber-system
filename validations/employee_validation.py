"""
Validation module for Employee entities.
"""

from typing import List
from database.models.service import Service
from repositories.service_repository import get_services_count, get_service
from repositories.employee_repository import search_employee_email
from custom_types.employee_type import EmployeeData
from validations.user_validation import UserValidation
from validations.validation_error import ValidationError


class EmployeeValidation(UserValidation):
    """
    Validation class for Employee entities.

    Extends UserValidation and adds additional checks, such as
    verifying whether an email is already registered in the Employee table.
    """

    @staticmethod
    def _email_exists(email: str) -> bool:
        """
        Checks if the given email is already registered in the Employee database.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if the email exists, False otherwise.
        """

        return search_employee_email(email) is not None

    @staticmethod
    def _services_is_empty() -> bool:
        """
        Checks if there is at least one registered Service 
        to associate to Employee.

        Returns:
            bool: True if there are no Services, False otherwise.
        """
        return get_services_count() == 0

    @staticmethod
    def _are_services_valid(services: List[Service]) -> bool:
        """
        Checks if the provided Services exists.

        Returns:
            bool: True if all Services were found, False otherwise.
        """

        return bool(services) and all(get_service(service_id=service) is not None for service in services)

    @staticmethod
    def validate_employee_data(data: EmployeeData) -> None:
        """
        Validates employee data.

        Args:
            data (EmployeeData): Data payload.

        Raises:
            ValidationError: If any fiels is missing.
        """

        required_fields = {'name', 'email', 'services'}

        if not all(field in data for field in required_fields):
            missing_fields = required_fields - data.keys()
            raise ValidationError(
                f"Missing fields: {', '.join(missing_fields)}")

    @staticmethod
    def validate_employee(name: str, email: str, services: list) -> None:
        """
        Validates employee.

        Args:
            name (str): The employee's name.
            email (str): The employee's email.

        Raises:
            ValidationError: If any validation fails.
        """

        UserValidation.validate_user_data(name, email)

        if EmployeeValidation._email_exists(email):
            raise ValidationError({'Employee': 'Email already registered.'})
        if EmployeeValidation._services_is_empty():
            raise ValidationError(
                {'Employee': 'A service must be registered before registering an employee'})
        if not EmployeeValidation._are_services_valid(services):
            raise ValidationError(
                {'Employee': 'Service not found.'})
