"""
Business module for Employee entities.
"""

from database.models.employee import Employee
from database.db_setup import db
from validations.employee_validation import EmployeeValidation


def create_employee(name: str, email: str) -> Employee:
    """
    Business class for creating a new Employee.

    Args:
        name (str): The name of the employee.
        email (str): The email of the employee.

    Returns:
        Employee: Created emplye.
    """

    EmployeeValidation.validate_employee_data(
        name, email)

    employee = Employee(name=name, email=email)
    db.session.add(employee)
    db.session.commit()

    return employee
