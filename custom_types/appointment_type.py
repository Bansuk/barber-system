"""
Type module for Appointment entities.
"""

from typing import List, TypedDict


class AppointmentData(TypedDict):
    """
    Type class for Appointment entities.
    """

    date: str
    customer_id: int
    employee_id: int
    services_ids: List[int]
