"""
Route module for Service routes.
"""

from flask import Blueprint, request, jsonify
from business.service_business import create_service
from validations.validation_error import ValidationError

service_bp = Blueprint('service', __name__)


@service_bp.route('/services', methods=['POST'])
def add_service():
    """
    Handles the creation of a new service.

    Receives a JSON payload with 'name' and 'price',
    calls the business logic to create a service,
    and returns an appropriate response.

    Returns:
        JSON response with success message (201) or validation errors (400).
    """

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    try:
        create_service(name, price)
        return jsonify({'message': 'Service added successfully'}), 201
    except ValidationError as e:
        return jsonify({'errors': e.get_errors()}), 400
