"""
Validation module for User entities.
"""

import re
from validations.validation_error import ValidationError


class UserValidation:
    """
    This class handles all validation logic for user data.
    """

    @staticmethod
    def _is_name_valid(name: str) -> bool:
        """
        Validate if the user name exists and if its length is larger than 3 characters.

        Args:
            name (str): The name to validate.

        Returns:
            bool: True if the name is valid, False otherwise.
        """

        return bool(name and len(name) >= 3)

    @staticmethod
    def _is_email_valid(email: str) -> bool:
        """
        Validate the user email format.

        Args:
            email (str): The email to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))

    @staticmethod
    def validate_user_data(name: str, email: str) -> dict:
        """
        Validate the user data (name and email).

        Args:
            name (str): The name to validate.
            email (str): The email to validate.

        Raises:
            ValidationError: If any validation fails.
        """

        if not UserValidation._is_name_valid(name):
            raise ValidationError({'User': 'Name format is invalid.'})
        if not UserValidation._is_email_valid(email):
            raise ValidationError({'User': 'Email format is invalid.'})
