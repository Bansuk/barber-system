"""
Business module for Customer entities.
"""

from database.models.customer import Customer
from database.db_setup import db
from validations.customer_validation import CustomerValidation


def create_customer(name: str, email: str) -> Customer:
    """
    Creates a new customer.

    Args:
        name (str): The name of the customer.
        email (str): The email of the customer.

    Returns:
        Customer: Created customer.
    """

    CustomerValidation.validate_customer(email)

    customer = Customer(name, email, appointments=[])

    try:
        db.session.add(customer)
        db.session.commit()

        return customer
    except Exception as error:
        db.session.rollback()
        raise error


def display_customer(customer: Customer) -> dict:
    """
   Converts the Customer instance into a dictionary format.

    Args:
        customer (Customer): A Customer object.

   Returns:
       dict: A dictionary containing customer details.
   """

    return {
        'id': customer.id,
        'name': customer.name,
        'email': customer.email,
    }
