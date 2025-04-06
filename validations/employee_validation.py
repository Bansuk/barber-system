"""
Validation module for Employee entities.
"""

from typing import List
from flask_smorest import abort
from database.models.service import Service
from repositories.service_repository import get_services_count, get_service
from repositories.employee_repository import search_employee_email


class EmployeeValidation():
    """
    Validation class for Employee entities.
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

        Args:
            services (List[Service]): List of Services.

        Returns:
            bool: True if all Services were found, False otherwise.
        """

        return bool(services) and all(get_service(service_id=service) is
                                      not None for service in services)

    @staticmethod
    def validate_employee(email: str, services: List[Service]) -> None:
        """
        Validates employee.

        Args:
            email (str): The employee's name.
            services (List[Service]): List of Services.

        Raises:
            HTTPException: If any validation fails.
        """

        if EmployeeValidation._email_exists(email):
            abort(409, message='Email already registered.')

        if EmployeeValidation._services_is_empty():
            abort(
                422, message='A service must be registered before registering an employee.')

        if not EmployeeValidation._are_services_valid(services):
            abort(404, message='Service not found.')
