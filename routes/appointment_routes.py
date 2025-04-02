"""
Route module for Appointment routes.
"""

from flask import Blueprint, request, jsonify
from business.appointment_business import create_appointment
from validations.validation_error import ValidationError

appointment_bp = Blueprint('appointment', __name__)


@appointment_bp.route('/appointments', methods=['POST'])
def add_appointment():
    """
    Handles the creation of a new appointment.

    Receives a JSON payload with 'name' and 'price',
    calls the business logic to create a appointment,
    and returns an appropriate response.

    Returns:
        JSON response with success message (201) or validation errors (400).
    """

    data = request.get_json()
    date = data.get('date')
    customer_id = data.get('customer_id')
    employee_id = data.get('employee_id')
    services_ids = data.get('services_ids')

    try:
        create_appointment(date, customer_id, employee_id, services_ids)
        return jsonify({'message': 'Appointment added successfully'}), 201
    except ValidationError as e:
        return jsonify({'errors': e.get_errors()}), 400
