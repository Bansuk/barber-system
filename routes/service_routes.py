"""
Route module for Service routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.service_schema import ServiceSchema, ServiceViewSchema
from business.service_business import create_service
from repositories.service_repository import get_all_services
from routes.docs.service_doc import (
    GET_SERVICE_SUMMARY,
    GET_SERVICE_DESCRIPTION,
    POST_SERVICE_SUMMARY,
    POST_SERVICE_DESCRIPTION,
    service_responses,
)


service_bp = SmorestBlueprint(
    'Service', __name__, description='Operações em Serviços')


@service_bp.route('/service', methods=['POST'])
@service_bp.arguments(ServiceSchema)
@service_bp.response(201, ServiceViewSchema, description='Serviço cadastrado com sucesso.')
@service_bp.doc(summary=POST_SERVICE_SUMMARY, description=POST_SERVICE_DESCRIPTION,
                responses=service_responses)
def add_service(service_data):
    """
    Handles the creation of a new service.

    This endpoint processes a form submission (JSON) to create a new service record.

    Receives a JSON payload with 'name' and 'price',
    calls the business logic to create a service,
    and returns an appropriate response.

    Returns:
        JSON response:
        - 201 (Created): Service created successfully.
        - 400 (Bad Request): Invalid body JSON format.
        - 409 (Conflict): Service already registered.
        - 422 (Unprocessable Entity): Validation error.
    """

    return create_service(**service_data)


@service_bp.route('/services', methods=['GET'])
@service_bp.response(200, ServiceViewSchema(many=True))
@service_bp.doc(summary=GET_SERVICE_SUMMARY, description=GET_SERVICE_DESCRIPTION)
def get_services():
    """
    Retrieve a list of all services.

    This endpoint returns a collection of services records in JSON format.

    Responses:         
        JSON response:
        - 200 (OK): Successfully retrieved the list of services.                                                     
    """

    return get_all_services()
