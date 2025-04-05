"""
Business module for Service entities.
"""

from database.models.service import Service
from database.db_setup import db
from validations.service_validation import ServiceValidation


def create_service(name: str, price: int) -> Service:
    """
    Creates a new Service.

    Args:
        name (str): The name of the service.
        price (str): The price of the service.

    Returns:
        Service: Created service.
    """

    ServiceValidation.validate_service(name, price)

    service = Service(name=name, price=price, employees=[], appointments=[])

    try:
        db.session.add(service)
        db.session.commit()

        return service
    except Exception as error:
        db.session.rollback()
        raise error
