"""
Schema module for Appointment entities.
"""

from marshmallow import Schema, fields, validate

DATE_METADATA = metadata = {
    'example': '2025-04-18 14:30:00'}
NAME_DESCRIPTION = 'Dia e hora do agendamento.'
CUSTOMER_METADATA = metadata = {
    'example': 1}
CUSTOMER_DESCRIPTION = 'ID do cliente que agendou o serviço.'
EMPLOYEE_METADATA = metadata = {
    'example': 1}
EMPLOYEE_DESCRIPTION = 'ID do funcionário(a) que irá executar o serviço.'


class AppointmentSchema(Schema):
    """
    Schema for validating and serializing Appointment input data.

    Attributes:
        date (datetime): The appointment's date.
        customer_id (int): The customer's ID.
        employee_id (int): The employee's ID.
        services_ids (List[int]): List of service IDs.
    """

    date = fields.Str(required=True, metadata=DATE_METADATA,
                      descriptiom=NAME_DESCRIPTION)
    customer_id = fields.Int(
        required=True, metadata=EMPLOYEE_METADATA, description=EMPLOYEE_DESCRIPTION)
    employee_id = fields.Int(
        required=True, metadata=CUSTOMER_METADATA, description=CUSTOMER_DESCRIPTION)
    services_ids = fields.List(
        fields.Int(),
        required=True,
        metadata={'example': '[1, 6]'},
        description='List of service IDs associated with the customer',
        validate=validate.Length(min=1, max=10)
    )


class AppointmentViewSchema(Schema):
    """
    Schema for serializing Appointment data for output.

    Attributes:
        id (int): The unique identifier of the appointment.
        date (datetime): The appointment's date.
        customer_id (int): The customer's ID.
        employee_id (int): The employee's ID.
        services_ids (List[int]): List of service IDs.
    """

    id = fields.Int(dump_only=True)
    date = fields.Str(required=True)
    customer_id = fields.Int()
    employee_id = fields.Int()
    services_ids = fields.List(
        fields.Pluck('ServiceViewSchema', 'id'),
        required=True,
        metadata={'example': '[1, 6]'},
        description='List of service IDs associated with the customer',
    )
