"""
Validation module for Customer entities.
"""

from repositories.customer_repository import search_customer_email
from custom_types.customer_type import CustomerData
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

        return search_customer_email(email) is not None

    @staticmethod
    def validate_customer_data(data: CustomerData) -> None:
        """
        Validates customer data.

        Args:
            data (CustomerData): Data payload.

        Raises:
            ValidationError: If any fiels is missing.
        """

        required_fields = {'name', 'email'}

        if not all(field in data for field in required_fields):
            missing_fields = required_fields - data.keys()
            raise ValidationError(
                f"Missing fields: {', '.join(missing_fields)}")

    @staticmethod
    def validate_customer(name: str, email: str) -> None:
        """
        Validates customer.

        Args:
            name (str): The customer's name.
            email (str): The customer's email.

        Raises:
            ValidationError: If any validation fails.
        """

        UserValidation.validate_user_data(name, email)

        if CustomerValidation._email_exists(email):
            raise ValidationError({'Customer': 'Email already registered.'})
