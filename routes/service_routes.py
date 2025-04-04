"""
Route module for Service routes.
"""

from flask import Blueprint, request, jsonify
from business.service_business import create_service
from repositories.service_repository import get_all_services
from validations.service_validation import ServiceValidation
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

    try:
        ServiceValidation.validate_service_data(data)
        create_service(**data)
        return jsonify({'message': 'Service added successfully'}), 201
    except ValidationError as error:
        return jsonify({'errors': error.get_errors()}), 400


@service_bp.route('/services', methods=['GET'])
def get_services():
    """
    Retrieves a list of all services.

    Returns:
        JSON response:
        - 200: List of services retrieved successfully.
    """

    services = get_all_services()
    return jsonify([service.to_dict() for service in services]), 200
