"""
Schema module for Employee entities.
"""

from marshmallow import Schema, fields, validate

NAME_METADATA = metadata = {
    'example': 'Corte de Cabelo Masculino'}
NAME_DESCRIPTION = 'Nome do Serviço'
PRICE_METADATA = metadata = {
    'example': '4500'}
PRICE_DESCRIPTION = 'Preço do Serviço'


class ServiceSchema(Schema):
    """
    Schema for validating and serializing service input data.

    Attributes:
        name (str): The name of the service (min 3, max 100 characters).
        price (int): The service's price.
    """

    name = fields.Str(required=True, metadata=NAME_METADATA,
                      descriptiom=NAME_DESCRIPTION, validate=validate.Length(min=3, max=100))
    price = fields.Int(
        required=True, metadata=PRICE_METADATA, description=PRICE_DESCRIPTION)


class ServiceViewSchema(Schema):
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
    name = fields.Str(required=True, metadata=NAME_METADATA,
                      descriptiom=NAME_DESCRIPTION)
    price = fields.Int(
        required=True, metadata=PRICE_METADATA, description=PRICE_DESCRIPTION)
    employees = fields.List(
        fields.Pluck('EmployeeViewSchema', 'id'),
        required=True,
        metadata={'example': '[1, 6]'},
        description='List of employees IDs associated with the service',
    )
    appointments = fields.List(
        fields.Pluck('AppointmentViewSchema', 'id'),
        required=True,
        metadata={'example': '[1, 6]'},
        description='List of appointments IDs associated containing the service',
    )
