"""
Type module for Employee entities.
"""

from typing import List, TypedDict
from database.models.service import Service
from database.models.appointment import Appointment


class EmployeeData(TypedDict):
    """
    Type class for Employee entities.
    """

    name: str
    email: int
    services: List[Service]
    appointments: List[Appointment]
