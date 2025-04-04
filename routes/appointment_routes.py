"""
Route module for Appointment routes.
"""

from flask import Blueprint, request, jsonify
from business.appointment_business import create_appointment
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
