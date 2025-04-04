"""
Route module for Customer routes.
"""

from flask import Blueprint, request, jsonify
from business.customer_business import create_customer
from repositories.customer_repository import get_all_customers
from validations.validation_error import ValidationError
from validations.customer_validation import CustomerValidation

customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/customers', methods=['POST'])
def add_customer():
    """
    Handles the creation of a new customer.

    Receives a JSON payload with 'name', 'email',
    calls the business logic to create a customer,
    and returns an appropriate response.

    Returns:
        JSON response:
        - 201: Customer created successfully.
        - 400: Validation error.
    """

    data = request.get_json()

    try:
        CustomerValidation.validate_customer_data(data)
        create_customer(**data)
        return jsonify({'message': 'Customer added successfully'}), 201
    except ValidationError as error:
        return jsonify({'errors': error.get_errors()}), 400


@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    """
    Retrieves a list of all customers.

    Returns:
        JSON response:
        - 200: List of customers retrieved successfully.
    """

    customers = get_all_customers()
    return jsonify([customer.to_dict() for customer in customers]), 200
