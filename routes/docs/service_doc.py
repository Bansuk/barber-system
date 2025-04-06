"""
This module contains standard descriptions and responses for the Service API.
"""

from schemas.error_schema import ErrorSchema


GET_SERVICE_SUMMARY = 'Retorna a lista de todos os serviços cadatrados.'
GET_SERVICE_DESCRIPTION = 'Este endpoint retorna uma coleção de serviços cadastrados ' \
    'no formato JSON.'
POST_SERVICE_SUMMARY = 'Lida com a criação de um novo serviço.'
POST_SERVICE_DESCRIPTION = 'Este endpoint processa o envio de um formulário (JSON) ' \
    'para criar um novo registro de serviço.'
service_responses = {
    400: {
        'description': 'Bad Request: O formato do corpo JSON é inválido.',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 400,
                    'errors': {
                        'json': [
                            'Invalid JSON body.'
                        ]
                    },
                    'status': 'Bad Request'
                }
            }
        }
    },
    409: {
        'description': 'Conflict: O serviço informado já está cadastrado.',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 409,
                    'errors': {
                        'json': {
                            'name': ['Service already registered.']
                        }
                    },
                    'status': 'Conflict'
                }
            }
        }
    },
    422: {
        'description':
        'Validation Error: A requisição contém campos ausentes ou inválidos.\n\n'
        '**Motivos Possíveis:**\n'
        '- `name` é obrigatório, mas não foi fornecido.\n'
        '- `price` é obrigatório, mas não foi fornecido.\n'
        '- `price`: o valor do serviço é inválido.\n\n',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 422,
                    'errors': {
                        'json': {
                            'name': ['Missing data for required field.'],
                            'price': ['Missing data for required field.',
                                      'Invalid price.']
                        }
                    },
                    'status': 'Unprocessable Entity'
                }
            }
        }
    }
}
