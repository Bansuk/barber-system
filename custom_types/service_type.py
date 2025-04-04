"""
Type module for Service entities.
"""

from typing import TypedDict


class ServiceData(TypedDict):
    """
    Type class for Service entities.
    """

    name: str
    price: int
