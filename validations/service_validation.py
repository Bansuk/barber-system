"""
Validation module for Service entities.
"""

from flask_smorest import abort
from repositories.service_repository import get_service_by_name

MAX_SERVICE_PRICE = 10000
MIN_SERVICE_PRICE = 2500


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
    def validate_service(name: str, price: int) -> None:
        """
        Validates service.

        Args:
            name (str): The service's name.
            price (int): The service's price.

        Raises:
            HTTPException: If any validation fails.
        """

        if ServiceValidation._is_service_already_registered(name):
            abort(409, message="Service is already registered.")

        if not ServiceValidation._is_price_in_valid_range(price):
            abort(422, message="Invalid price.")
