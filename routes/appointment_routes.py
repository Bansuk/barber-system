"""
Route module for Appointment routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.appointment_schema import AppointmentSchema, AppointmentViewSchema
from business.appointment_business import create_appointment
from repositories.appointment_repository import get_all_appointments

appointment_bp = SmorestBlueprint(
    'appointment', __name__, description='Operations on appointments')


@appointment_bp.route('/appointments', methods=['POST'])
@appointment_bp.arguments(AppointmentSchema)
@appointment_bp.response(201, AppointmentViewSchema, description='Appointment successfully created')
def add_appointment(apointment_data):
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

    return create_appointment(**apointment_data)


@appointment_bp.route('/appointments', methods=['GET'])
@appointment_bp.response(200, AppointmentViewSchema(many=True))
def get_appointments():
    """
    Retrieves a list of all appointments.

    Returns:
        JSON response:
        - 200: List of appointments retrieved successfully.
    """

    return get_all_appointments()
