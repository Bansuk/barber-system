"""
Schema module for Appointment entities.
"""

from marshmallow import Schema, fields, validate

DATE_METADATA = metadata = {
    'example': '2025-04-04 14:30:00'}
NAME_DESCRIPTION = 'Dia e hora do agendamento.'
CUSTOMER_METADATA = metadata = {
    'example': 1}
CUSTOMER_DESCRIPTION = 'ID do cliente que agendou o serviço.'
EMPLOYEE_METADATA = metadata = {
    'example': 1}
EMPLOYEE_DESCRIPTION = 'ID do funcionário(a) que irá executar o serviço.'


class AppointmentSchema(Schema):
    """
    Schema for validating and serializing service input data.

    Attributes:
        name (str): The name of the service (min 3, max 100 characters).
        price (int): The service's price.
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
    Schema for serializing employee data for output.

    Attributes:
        id (int): The unique identifier of the employee.
        name (str): The name of the employee.
        email (str): The employee's email address.
        employees (List[int]): The list of employees that can performe the service.
        appointment (List[int]): The list of appointment containing the service.
    """

    id = fields.Int(dump_only=True)
    date = fields.Str(required=True)
    employee_id = fields.Int()
    customer_id = fields.Int()
    services_ids = fields.List(
        fields.Pluck('ServiceViewSchema', 'id'),
        required=True,
        metadata={'example': '[1, 6]'},
        description='List of service IDs associated with the customer',
    )
