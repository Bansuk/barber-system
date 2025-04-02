"""
Business module for Service entities.
"""
from typing import List
from database.models.service import Service
from database.db_setup import db
from validations.service_validation import ServiceValidation


def create_service(name: str, price: int) -> Service:
    """
    Business class for creating a new Service.

    Args:
        name (str): The name of the service.
        price (str): The price of the service.

    Returns:
        Service: Created service.
    """

    ServiceValidation.validate_service_data(
        name, price)

    service = Service(name=name, price=price, employees=[], appointments=[])
    db.session.add(service)
    db.session.commit()

    return service


def get_services() -> List[Service]:
    """
    Business class for getting all 
     registered Services.

    Returns:
        List[Service]: A List of registered services.
    """

    return db.session.query(Service).all()


def get_services_count() -> int:
    """
    Business class for getting the number
     of registered Services.

    Returns:
        int: The number of registered services.
    """

    return db.session.query(Service).count()


def get_service(service_id) -> Service:
    """
    Business class for getting a Service by its id.

    Returns:
        Service: The service found.
    """

    return db.session.query(Service).filter_by(id=service_id).first()
