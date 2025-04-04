"""
Route module for Customer routes.
"""

from flask import Blueprint, request, jsonify
from business.customer_business import create_customer
from validations.validation_error import ValidationError
from validations.customer_validation import CustomerValidation

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/customers", methods=["POST"])
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
    except ValidationError as e:
        return jsonify({'errors': e.get_errors()}), 400
