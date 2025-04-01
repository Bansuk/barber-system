"""
Route module for Customer routes.
"""

from flask import Blueprint, request, jsonify
from business.customer_business import create_customer
from validations.validation_error import ValidationError

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/customers", methods=["POST"])
def add_customer():
    """
    Handles the creation of a new customer.

    Receives a JSON payload with 'name' and 'email',
    calls the business logic to create a customer,
    and returns an appropriate response.

    Returns:
        JSON response with success message (201) or validation errors (400).
    """

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    try:
        create_customer(name, email)
        return jsonify({'message': 'Customer added successfully'}), 201
    except ValidationError as e:
        return jsonify({'errors': e.get_errors()}), 400
