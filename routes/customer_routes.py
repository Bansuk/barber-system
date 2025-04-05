"""
Route module for Customer routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.customer_schema import CustomerSchema, CustomerViewSchema
from business.customer_business import create_customer
from repositories.customer_repository import get_all_customers

customer_bp = SmorestBlueprint(
    'Customer', __name__, description='Operations on customers')


@customer_bp.route('/customer', methods=['POST'])
@customer_bp.arguments(CustomerSchema)
@customer_bp.response(201, CustomerViewSchema, description='Customer successfully created')
def add_customer(customer_data):
    """
    Handles the creation of a new customer.

    This endpoint processes a form submission to create a new customer record.

    Responses:                                                              

        201 Created:
        - Customer successfully created.
        - The response body contains the newly created customer object.

        409 Conflict:
        - Email already registered.
        - The response body contains an error message.

        422 Unprocessable Entity:
        - Validation error (e.g., invalid email format).
        - The response body contains details about the issue.
    """

    return create_customer(**customer_data)


@customer_bp.route('/customers', methods=['GET'])
@customer_bp.response(200, CustomerViewSchema(many=True))
def get_customers():
    """
    Retrieve a list of all customers.

    This endpoint returns a collection of customer records in JSON format.

    Responses:

        200 OK: 
        - Successfully retrieved the list of customers.
        - The response body contains an array of customer objects.
    """

    return get_all_customers()
