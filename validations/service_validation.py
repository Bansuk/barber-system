"""
Validation module for Service entities.
"""

from custom_types.service_type import ServiceData
from repositories.service_repository import get_service_by_name
from validations.validation_error import ValidationError


class ServiceValidation():
    """
    Validation class for Service entities.
    """

    @staticmethod
    def _is_price_in_valid_range(price: int) -> bool:
        """
        Checks if the given price is inside the specified price range.

        Args:
            price (int): The price to check.

        Returns:
            bool: True if the price is in valid price range, False otherwise.
        """

        MAX_SERVICE_PRICE = 10000
        MIN_SERVICE_PRICE = 2500

        return MIN_SERVICE_PRICE <= price <= MAX_SERVICE_PRICE

    @staticmethod
    def _is_service_already_registered(name: str) -> bool:
        """
        Checks if the given service is already registered in the Service database.

        Args:
            name (str): The service name to check.

        Returns:
            bool: True if the service exists, False otherwise.
        """

        return get_service_by_name(name) is not None

    @staticmethod
    def validate_service_data(data: ServiceData) -> None:
        """
        Validates service data.

        Args:
            data (ServiceData): Data payload.

        Raises:
            ValidationError: If any fiels is missing.
        """

        required_fields = {'name', 'price'}

        if not all(field in data for field in required_fields):
            missing_fields = required_fields - data.keys()
            raise ValidationError(
                f"Missing fields: {', '.join(missing_fields)}")

    @staticmethod
    def validate_service(name: str, price: int) -> None:
        """
        Validates service.

        Args:
            name (str): The service's name.
            price (int): The service's price.

        Raises:
            ValidationError: If any validation fails.
        """

        if ServiceValidation._is_service_already_registered(name):
            raise ValidationError(
                {'Service': 'Service is already registered.'})
        if not ServiceValidation._is_price_in_valid_range(price):
            raise ValidationError({'Service': 'Invalid price.'})
