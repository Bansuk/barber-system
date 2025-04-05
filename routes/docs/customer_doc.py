"""
This module contains standard descriptions and responses for the customer API.
"""

from schemas.error_schema import ErrorSchema


GET_CUSTOMER_SUMMARY = 'Retorna a lista de todos os clientes cadatrados.'
GET_CUSTOMER_DESCRIPTION = 'Este endpoint retorna uma coleção de cadastros de clientes ' \
    'no formato JSON'
POST_CUSTOMER_SUMMARY = 'Lida com a criação de um novo cliente.'
POST_CUSTOMER_DESCRIPTION = 'Este endpoint processa o envio de um formulário (JSON) ' \
    'para criar um novo registro de cliente.'
customer_responses = {
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
        'description': 'Conflict: O email fornecido já está em uso. Por favor, '
        'forneça um email diferente.',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 409,
                    'errors': {
                        'json': {
                            'email': ['Email already registered.']
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
        '- `email` é obrigatório, mas não foi fornecido.\n'
        '- `email`: o formato do email é inválido (deve ser um endereço de e-mail válido).\n\n',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 422,
                    'errors': {
                        'json': {
                            'name': ['Missing data for required field.'],
                            'email': ['Missing data for required field.',
                                      'Not a valid email address.']
                        }
                    },
                    'status': 'Unprocessable Entity'
                }
            }
        }
    }
}
