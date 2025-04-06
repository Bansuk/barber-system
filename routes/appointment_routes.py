"""
Route module for Appointment routes.
"""

from flask_smorest import Blueprint as SmorestBlueprint
from schemas.appointment_schema import AppointmentSchema, AppointmentViewSchema
from business.appointment_business import create_appointment
from repositories.appointment_repository import get_all_appointments
from routes.docs.appointment_doc import (
    GET_APPOINTMENT_SUMMARY,
    GET_APPOINTMENT_DESCRIPTION,
    POST_APPOINTMENT_SUMMARY,
    POST_APPOINTMENT_DESCRIPTION,
    appointment_responses,
)

appointment_bp = SmorestBlueprint(
    'Appointment', __name__, description='Operações em Agendamentos')


@appointment_bp.route('/appointment', methods=['POST'])
@appointment_bp.arguments(AppointmentSchema)
@appointment_bp.response(201, AppointmentViewSchema, description='Agendamento realizado com sucesso.')
@appointment_bp.doc(summary=POST_APPOINTMENT_SUMMARY, description=POST_APPOINTMENT_DESCRIPTION,
                    responses=appointment_responses)
def add_appointment(apointment_data):
    """
    Handles the creation of a new appointment.

    This endpoint processes a form submission (JSON) to create a new appointment record.


    Receives a JSON payload with 'date', 'customer_id', 'employee_id', and 'services_ids',
    calls the business logic to create an appointment,
    and returns an appropriate response.

    Returns:
        JSON response:
        - 201 (Created): Appointment created successfully.
        - 400 (Bad Request): Invalid body JSON format/Invalid date.
        - 409 (Conflict): Date already booked.
        - 422 (Unprocessable Entity): Validation error.
    """

    return create_appointment(**apointment_data)


@appointment_bp.route('/appointments', methods=['GET'])
@appointment_bp.response(200, AppointmentViewSchema(many=True))
@appointment_bp.doc(summary=GET_APPOINTMENT_SUMMARY, description=GET_APPOINTMENT_DESCRIPTION)
def get_appointments():
    """
    Retrieves a list of all appointments.

    This endpoint returns a collection of appointments records in JSON format.

    Responses:         
        JSON response:
        - 200 (OK): Successfully retrieved the list of appointments.
    """

    return get_all_appointments()
