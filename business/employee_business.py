"""
Business module for Employee entities.
"""

from typing import List
from database.models.employee import Employee
from database.db_setup import db
from repositories.service_repository import get_services_by_services_ids
from validations.employee_validation import EmployeeValidation


def create_employee(name: str, email: str, services: List[int]) -> Employee:
    """
    Creates a new Employee.

    Args:
        name (str): The name of the employee.
        email (str): The email of the employee.
        services (List): The list of services performed by the employee.

    Returns:
        Employee: Created employee.
    """

    EmployeeValidation.validate_employee(
        name, email, services)

    services = get_services_by_services_ids(services_ids=services)

    employee = Employee(name, email, services, appointments=[])

    try:
        db.session.add(employee)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        raise error

    return employee
