"""
Repository module for Service queries.
"""

from typing import List, Optional
from database.models.service import Service
from database.db_setup import db


def get_all_services() -> List[Service]:
    """
    Retrieves all registered services.

    Returns:
        List[Service]: A List of registered services.
    """

    return db.session.query(Service).all()


def get_services_by_services_ids(services_ids: List[int]) -> List[Service]:
    """
    Retrieves all registered services by ID's.


    Args:
        services_ids (List[int]): The services ID's to search.

    Returns:
        List[Service]: A List of registered services.
    """

    return db.session.query(Service).filter(Service.id.in_(services_ids)).all()


def get_services_count() -> int:
    """
    Retrieves the number of registered services.

    Returns:
        int: The total number of services.
    """

    return db.session.query(Service).count()


def get_service(service_id: int) -> Optional[Service]:
    """
    Retrieves a service by its ID.

    Args:
        service_id (int): The service ID.

    Returns:
        Service: The service found or None.
    """

    return db.session.query(Service).filter_by(id=service_id).first()


def get_service_by_name(name: str) -> Optional[Service]:
    """
    Retrieves a service by its name.

    Args:
        name (str): The service name.

    Returns:
        Service: The service found or None.
    """

    return db.session.query(Service.name).filter_by(name=name).first()
