"""
Schema module for Error entities.
"""

from marshmallow import Schema, fields


class ErrorDetailSchema(Schema):
    """
    Schema for detailed error messages.

    Attributes:
        json (Dict[str, List[str]]): A dictionary where keys are field names
            and values are lists of error messages related to those fields.
    """

    json = fields.Dict(keys=fields.String(), values=fields.List(
        fields.String()), required=True)


class ErrorSchema(Schema):
    """
    Schema for representing error responses.

    Attributes:
        code (int): The HTTP status code associated with the error.
        errors (ErrorDetailSchema): Nested schema containing detailed error messages.
        status (str): A short textual description of the error.
    """

    code = fields.Integer(required=True, description='HTTP status code')
    errors = fields.Nested(ErrorDetailSchema, required=True,
                           description='Detailed error messages')
    status = fields.String(required=True, description='Error status text')
