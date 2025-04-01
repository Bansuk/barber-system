"""
Registers the customer-related routes with the Flask application.
"""

from flask import Flask
from routes.customer_routes import customer_bp
from routes.employee_routes import employee_bp


def register_routes(app: Flask):
    """
    Registers all application routes.

    Args:
        app (Flask): The Flask application instance.
    """

    app.register_blueprint(customer_bp)
    app.register_blueprint(employee_bp)
