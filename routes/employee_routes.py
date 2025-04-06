"""
Route module for Employee routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.employee_schema import EmployeeSchema, EmployeeViewSchema
from business.employee_business import create_employee
from repositories.employee_repository import get_all_employees
from routes.docs.employee_doc import (
    GET_EMPLOYEE_SUMMARY,
    GET_EMPLOYEE_DESCRIPTION,
    POST_EMPLOYEE_SUMMARY,
    POST_EMPLOYEE_DESCRIPTION,
    employee_responses,
)

employee_bp = SmorestBlueprint(
    'Employee', __name__, description='Operações em Funcionários')


@employee_bp.route('/employee', methods=['POST'])
@employee_bp.arguments(EmployeeSchema)
@employee_bp.doc(summary=POST_EMPLOYEE_SUMMARY, description=POST_EMPLOYEE_DESCRIPTION,
                 responses=employee_responses)
@employee_bp.response(201, EmployeeViewSchema, description='Funcionário(a) cadastrado com sucesso.')
def add_employee(employee_data):
    """
    Handles the creation of a new employee.

    This endpoint processes a form submission (JSON) to create a new employee record.

    Receives a JSON payload with 'name', 'email' and 
    'services, calls the business logic to create a 
    employee, and returns an appropriate response.

    Returns:
        JSON response:
        - 201 (Created): Employee created successfully.
        - 400 (Bad Request): Invalid body JSON format.
        - 404 (Not Found): Service not found.
        - 409 (Conflict): Email already registered.
        - 422 (Unprocessable Entity): Validation error.
    """

    return create_employee(**employee_data)


@employee_bp.route('/employees', methods=['GET'])
@employee_bp.response(200, EmployeeViewSchema(many=True))
@employee_bp.doc(summary=GET_EMPLOYEE_SUMMARY, description=GET_EMPLOYEE_DESCRIPTION)
def get_employees():
    """
    Retrieves a list of all employees.

    Returns:
        JSON response:
        - 200: List of employees retrieved successfully.
    """

    return get_all_employees()
