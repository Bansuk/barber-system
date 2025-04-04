"""
Type module for Employee entities.
"""

from typing import List, TypedDict


class EmployeeData(TypedDict):
    """
    Type class for Employee entities.
    """

    name: str
    email: int
    services: List[int]
