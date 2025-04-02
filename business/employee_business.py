"""
Business module for Employee entities.
"""

from database.models.service import Service
from database.models.employee import Employee
from database.db_setup import db
from validations.employee_validation import EmployeeValidation


def create_employee(name: str, email: str, service_ids: list) -> Employee:
    """
    Business class for creating a new Employee.

    Args:
        name (str): The name of the employee.
        email (str): The email of the employee.
        services (List): The list of services performed by the employee.

    Returns:
        Employee: Created employee.
    """

    EmployeeValidation.validate_employee_data(
        name, email, service_ids)

    services = Service.query.filter(Service.id.in_(service_ids)).all()

    employee = Employee(name, email, services, appointments=[])
    db.session.add(employee)
    db.session.commit()

    return employee
