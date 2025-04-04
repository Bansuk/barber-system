"""
Validation module for Employee entities.
"""

from database.models import Employee
from database.db_setup import db
from validations.user_validation import UserValidation
from validations.validation_error import ValidationError
from repositories.service_repository import get_services_count, get_service


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

        return db.session.query(Employee.id).filter_by(email=email).first() is not None

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
    def _are_services_not_valid(services) -> bool:
        """
        Checks if there is at least one registered Service 
        to associate to Employee.

        Returns:
            bool: True if there are no Services, False otherwise.
        """

        for service in services:
            found_service = get_service(service_id=service)

            if found_service is None:
                return True

        return False

    @staticmethod
    def validate_employee_data(name: str, email: str, service_ids: list):
        """
        Validates employee data.

        Args:
            name (str): The employee's name.
            email (str): The employee's email.

        Raises:
            ValidationError: If provided email already exists.
        """

        UserValidation.validate_user_data(name, email)

        if EmployeeValidation._email_exists(email):
            raise ValidationError({'email': 'Email ja cadastrado.'})
        if EmployeeValidation._services_is_empty():
            raise ValidationError(
                {'service': 'Nao e possivel cadastrar um funcionario(a) '
                 'sem cadastrar um servico primeiro.'})
        if EmployeeValidation._are_services_not_valid(service_ids):
            raise ValidationError(
                {'service': 'Servico informado nao foi encontrado.'})
