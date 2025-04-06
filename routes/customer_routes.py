"""
Route module for Customer routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.customer_schema import CustomerSchema, CustomerViewSchema
from business.customer_business import create_customer
from repositories.customer_repository import get_all_customers
from routes.docs.customer_doc import (
    GET_CUSTOMER_SUMMARY,
    GET_CUSTOMER_DESCRIPTION,
    POST_CUSTOMER_SUMMARY,
    POST_CUSTOMER_DESCRIPTION,
    customer_responses,
)

customer_bp = SmorestBlueprint(
    'Customer', __name__, description='Operações em Clientes')


@customer_bp.route('/customer', methods=['POST'])
@customer_bp.arguments(CustomerSchema)
@customer_bp.response(201, CustomerViewSchema, description='Cliente cadastrado com sucesso.')
@customer_bp.doc(summary=POST_CUSTOMER_SUMMARY, description=POST_CUSTOMER_DESCRIPTION,
                 responses=customer_responses)
def add_customer(customer_data):
    """
    Handles the creation of a new customer.

    This endpoint processes a form submission (JSON) to create a new customer record.

    Receives a JSON payload with 'name', and 'email',
    calls the business logic to create a customer,
    and returns an appropriate response.

    Returns:
        JSON response:
        - 201 (Created): Customer created successfully.
        - 400 (Bad Request): Invalid body JSON format.
        - 409 (Conflict): Email already registered.
        - 422 (Unprocessable Entity): Validation error.
    """

    return create_customer(**customer_data)


@customer_bp.route('/customers', methods=['GET'])
@customer_bp.response(200, CustomerViewSchema(many=True))
@customer_bp.doc(summary=GET_CUSTOMER_SUMMARY, description=GET_CUSTOMER_DESCRIPTION)
def get_customers():
    """
    Retrieve a list of all customers.

    This endpoint returns a collection of customer records in JSON format.

    Responses:         
        JSON response:
        - 200 (OK): Successfully retrieved the list of customers.                                                     
    """

    return get_all_customers()
