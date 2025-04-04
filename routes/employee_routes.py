"""
Route module for Employee routes.
"""

from flask import Blueprint, request, jsonify
from business.employee_business import create_employee
from repositories.employee_repository import get_all_employees
from validations.employee_validation import EmployeeValidation
from validations.validation_error import ValidationError

employee_bp = Blueprint('employee', __name__)


@employee_bp.route('/employees', methods=['POST'])
def add_employee():
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

    data = request.get_json()

    try:
        EmployeeValidation.validate_employee_data(data)
        create_employee(**data)
        return jsonify({'message': 'Employee added successfully'}), 201
    except ValidationError as error:
        return jsonify({'errors': error.get_errors()}), 400


@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    """
    Retrieves a list of all employees.

    Returns:
        JSON response:
        - 200: List of employees retrieved successfully.
    """

    employees = get_all_employees()
    return jsonify([employee.to_dict() for employee in employees]), 200
