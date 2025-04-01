"""
Route module for Employee routes.
"""

from flask import Blueprint, request, jsonify
from business.employee_business import create_employee
from validations.validation_error import ValidationError

employee_bp = Blueprint('employee', __name__)


@employee_bp.route("/employees", methods=['POST'])
def add_employee():
    """
    Handles the creation of a new employee.

    Receives a JSON payload with 'name' and 'email',
    calls the business logic to create a employee,
    and returns an appropriate response.

    Returns:
        JSON response with success message (201) or validation errors (400).
    """

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    try:
        create_employee(name, email)
        return jsonify({'message': 'Employee added successfully'}), 201
    except ValidationError as e:
        return jsonify({'errors': e.get_errors()}), 400
