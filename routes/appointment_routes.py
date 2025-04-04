"""
Route module for Appointment routes.
"""

from flask import Blueprint, request, jsonify
from business.appointment_business import create_appointment
from repositories.appointment_repository import get_all_appointments
from validations.validation_error import ValidationError
from validations.appointment_validation import AppointmentValidation

appointment_bp = Blueprint('appointment', __name__)


@appointment_bp.route('/appointments', methods=['POST'])
def add_appointment():
    """
    Handles the creation of a new appointment.

    Receives a JSON payload with 'date', 'customer_id', 'employee_id', and 'services_ids',
    calls the business logic to create an appointment,
    and returns an appropriate response.

    Returns:
        JSON response:
        - 201: Appointment created successfully.
        - 400: Validation error.
    """

    data = request.get_json()

    try:

        AppointmentValidation.validate_appointment_data(data)
        create_appointment(**data)
        return jsonify({'message': 'Appointment added successfully'}), 201
    except ValidationError as error:
        return jsonify({'errors': error.get_errors()}), 400


@appointment_bp.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Retrieves a list of all appointments.

    Returns:
        JSON response:
        - 200: List of appointments retrieved successfully.
    """

    appointments = get_all_appointments()
    return jsonify([appointment.to_dict() for appointment in appointments]), 200
