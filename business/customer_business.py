"""
Business module for Customer entities.
"""

from database.models.customer import Customer
from database.db_setup import db
from validations.customer_validation import CustomerValidation


def create_customer(name: str, email: str) -> Customer:
    """
    Business class for creating a new Customer.

    Args:
        name (str): The name of the customer.
        email (str): The email of the customer.

    Returns:
        Customer: Created customer.
    """

    CustomerValidation.validate_customer_data(
        name, email)

    customer = Customer(name, email, appointments=[])
    db.session.add(customer)
    db.session.commit()

    return customer


def get_customer(customer_id) -> Customer:
    """
    Business class for getting an Customer by its id.

    Returns:
        Customer: The customer found.
    """

    return db.session.query(Customer).filter_by(id=customer_id).first()
