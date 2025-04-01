"""
Validation module for Employee entities.
"""

from database.models import Employee
from database.db_setup import db
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

        return db.session.query(Employee.id).filter_by(email=email).first() is not None

    @staticmethod
    def validate_employee_data(name: str, email: str):
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
