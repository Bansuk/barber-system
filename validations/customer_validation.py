"""
Validation module for Customer entities.
"""

from database.models import Customer
from database.db_setup import db
from validations.user_validation import UserValidation
from validations.validation_error import ValidationError


class CustomerValidation(UserValidation):
    """
    Validation class for Customer entities.

    Extends UserValidation and adds additional checks, such as
    verifying whether an email is already registered in the Customer table.
    """

    @staticmethod
    def _email_exists(email: str) -> bool:
        """
        Checks if the given email is already registered in the Customer database.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if the email exists, False otherwise.
        """

        return db.session.query(Customer.id).filter_by(email=email).first() is not None

    @staticmethod
    def validate_customer_data(name: str, email: str):
        """
        Validates customer data.

        Args:
            name (str): The customer's name.
            email (str): The customer's email.

        Raises:
            ValidationError: If provided email already exists.
        """

        UserValidation.validate_user_data(name, email)

        if CustomerValidation._email_exists(email):
            raise ValidationError({"email": "Email ja cadastrado."})
