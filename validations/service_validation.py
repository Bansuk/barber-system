"""
Validation module for Service entities.
"""

from database.models import Service
from database.db_setup import db
from validations.validation_error import ValidationError


class ServiceValidation():
    """
    Validation class for Service entities.
    """

    @staticmethod
    def _is_price_in_invalid_range(price: int) -> bool:
        """
        Checks if the given price is inside the specified price range.

        Args:
            price (int): The price to check.

        Returns:
            bool: True if the price is in valid price range, False otherwise.
        """

        MAX_SERVICE_PRICE = 10000
        MIN_SERVICE_PRICE = 2500

        if price < MIN_SERVICE_PRICE or price > MAX_SERVICE_PRICE:
            return True
        return False

    @staticmethod
    def _is_service_already_registered(name: str) -> bool:
        """
        Checks if the given service is already registered in the Service database.

        Args:
            name (str): The service name to check.

        Returns:
            bool: True if the service exists, False otherwise.
        """

        return db.session.query(Service.id).filter_by(name=name).first() is not None

    @staticmethod
    def validate_service_data(name: str, price: int):
        """
        Validates service data.

        Args:
            name (str): The service's name.
            price (int): The service's price.

        Raises:
            ValidationError: If provided service already exists or provided price is out of range.
        """

        if ServiceValidation._is_service_already_registered(name):
            raise ValidationError({'service': 'Servico ja cadastrado.'})
        if ServiceValidation._is_price_in_invalid_range(price):
            raise ValidationError({'price': 'Preco invalido.'})
