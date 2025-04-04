"""
Repository module for Service queries.
"""

from typing import List
from database.models.service import Service
from database.db_setup import db


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
