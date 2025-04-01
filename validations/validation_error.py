"""
Module for handling validation errors.
"""


class ValidationError(Exception):
    """
    Custom exception to represent validation errors.
    """

    def __init__(self, errors: dict):
        """
        Initializes the ValidationError with error details.

        Args:
            errors (dict): A dictionary containing the validation errors.
        """

        self.errors = errors

    def get_errors(self) -> dict:
        """
        Returns the validation errors.

        Returns:
            dict: The validation errors.
        """

        return self.errors
