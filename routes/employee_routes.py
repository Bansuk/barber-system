"""
Route module for Employee routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.employee_schema import EmployeeSchema, EmployeeViewSchema
from business.employee_business import create_employee
from repositories.employee_repository import get_all_employees

employee_bp = SmorestBlueprint(
    'Employee', __name__, description='Operations on employees')


@employee_bp.route('/employees', methods=['POST'])
@employee_bp.arguments(EmployeeSchema)
@employee_bp.response(201, EmployeeViewSchema, description='Employee successfully created')
def add_employee(employee_data):
    """
    Handles the creation of a new employee.

    Receives a JSON payload with 'name', 'email' and 
    'services;, calls the business logic to create a 
    employee, and returns an appropriate response.

    Returns:
        JSON response:
        - 201: Employee created successfully.
        - 400: Validation error.
    """

    return create_employee(**employee_data)


@employee_bp.route('/employees', methods=['GET'])
@employee_bp.response(200, EmployeeViewSchema(many=True))
def get_employees():
    """
    Retrieves a list of all employees.

    Returns:
        JSON response:
        - 200: List of employees retrieved successfully.
    """

    return get_all_employees()
