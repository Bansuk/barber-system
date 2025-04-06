"""
Schema module for Appointment entities.
"""

from marshmallow import Schema, fields, validate

DATE_METADATA = metadata = {
    'example': '2025-04-18 14:30:00'}
DATE_DESCRIPTION = 'Dia e hora do agendamento. ' \
    '(Não pode ser no passado e nem a mais de 7 dias no futuro.)' \
    '(Horário selecionado deve estar entre 09:00 e 18:00.)'
CUSTOMER_METADATA = metadata = {
    'example': 1}
CUSTOMER_DESCRIPTION = 'ID do cliente que agendou o serviço.'
EMPLOYEE_METADATA = metadata = {
    'example': 1}
EMPLOYEE_DESCRIPTION = 'ID do funcionário(a) que irá executar o serviço.'
SERVICES_METADATA = metadata = {
    'example': [1]}
SERVICES_DESCRIPTION = 'Lista de serviços do agendamento.'


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
                      description=DATE_DESCRIPTION)
    customer_id = fields.Int(
        required=True, metadata=EMPLOYEE_METADATA, description=EMPLOYEE_DESCRIPTION)
    employee_id = fields.Int(
        required=True, metadata=CUSTOMER_METADATA, description=CUSTOMER_DESCRIPTION)
    services_ids = fields.List(
        fields.Int(),
        required=True,
        metadata=SERVICES_METADATA,
        description=SERVICES_DESCRIPTION,
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
        metadata=SERVICES_METADATA,
        description=SERVICES_DESCRIPTION,
    )
