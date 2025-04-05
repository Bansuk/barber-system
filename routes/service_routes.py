"""
Route module for Service routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.service_schema import ServiceSchema, ServiceViewSchema
from business.service_business import create_service
from repositories.service_repository import get_all_services

service_bp = SmorestBlueprint(
    'Service', __name__, description='Operations on services')


@service_bp.route('/services', methods=['POST'])
@service_bp.arguments(ServiceSchema)
@service_bp.response(201, ServiceViewSchema, description='Service successfully created')
def add_service(service_data):
    """
    Handles the creation of a new service.

    Receives a JSON payload with 'name' and 'price',
    calls the business logic to create a service,
    and returns an appropriate response.

    Returns:
        JSON response with success message (201) or validation errors (400).
    """

    return create_service(**service_data)


@service_bp.route('/services', methods=['GET'])
@service_bp.response(200, ServiceViewSchema(many=True))
def get_services():
    """
    Retrieves a list of all services.

    Returns:
        JSON response:
        - 200: List of services retrieved successfully.
    """

    return get_all_services()
