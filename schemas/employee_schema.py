"""
Schema module for Employee entities.
"""

from marshmallow import Schema, fields, validate

NAME_METADATA = metadata = {
    'example': 'Fulano de Tal'}
NAME_DESCRIPTION = 'Nome do Funcionário(a)'
EMAIL_METADATA = {
    'example': 'fulano@teste.com'}
EMAIL_DESCRIPTION = 'E-mail do Funcionário(a)'


class EmployeeSchema(Schema):
    """
    Schema for validating and serializing employee input data.

    Attributes:
        name (str): The name of the employee (min 3, max 100 characters).
        email (str): The employee's email address.
        services (List[int]): The list of services performed by the employee.
    """

    name = fields.Str(required=True, metadata=NAME_METADATA,
                      descriptiom=NAME_DESCRIPTION, validate=validate.Length(min=3, max=100))
    email = fields.Email(
        required=True, metadata=EMAIL_METADATA, description=EMAIL_DESCRIPTION)
    services = fields.List(
        fields.Int(),
        required=True,
        metadata={'example': '[1]'},
        description='Lista dos serviços executados pelo funcinário(a)',
        validate=validate.Length(min=1, max=10)
    )


class EmployeeViewSchema(Schema):
    """
    Schema for serializing employee data for output.

    Attributes:
        id (int): The unique identifier of the employee.
        name (str): The name of the employee.
        email (str): The employee's email address.
        services (List[int]): The list of services performed by the employee.
    """

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, metadata=NAME_METADATA,
                      description=NAME_DESCRIPTION)
    email = fields.Email(
        required=True, metadata=EMAIL_METADATA, description=EMAIL_DESCRIPTION)
    services = fields.List(
        fields.Pluck('ServiceViewSchema', 'id'),
        required=True,
        metadata={'example': '[1]'},
        description='Lista dos serviços executados pelo funcinário(a)',
    )
