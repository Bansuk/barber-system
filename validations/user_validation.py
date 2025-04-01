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
    def _validate_name(name: str) -> bool:
        """
        Validate if the user name exists and if its length is larger than 3 characters.

        Args:
            name (str): The name to validate.

        Returns:
            bool: True if the name is valid, False otherwise.
        """

        return bool(name and len(name) >= 3)

    @staticmethod
    def _validate_email(email: str) -> bool:
        """
        Validate the user email.

        Args:
            email (str): The email to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))

    @classmethod
    def validate_user_data(cls, name: str, email: str) -> dict:
        """
        Validate the user data (name and email).

        Args:
            name (str): The name to validate.
            email (str): The email to validate.

        Raises:
            ValidationError: If any validation fails.
        """
        errors = {}

        if not cls._validate_name(name):
            errors['name'] = 'O nome precisa ter no minimo 3 caracteres.'
        if not cls._validate_email(email):
            errors['email'] = 'Formato de e-mail invalido.'

        if errors:
            raise ValidationError(errors)
