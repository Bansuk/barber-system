"""
This module contains standard descriptions and responses for the Employee API.
"""

from schemas.error_schema import ErrorSchema


GET_EMPLOYEE_SUMMARY = 'Retorna a lista de todos os funcionários cadatrados.'
GET_EMPLOYEE_DESCRIPTION = 'Este endpoint retorna uma coleção de cadastros de funcionários ' \
    'no formato JSON.'
POST_EMPLOYEE_SUMMARY = 'Lida com a criação de um novo funcionário(a).'
POST_EMPLOYEE_DESCRIPTION = 'Este endpoint processa o envio de um formulário (JSON) ' \
    'para criar um novo registro de funcionário(a).'
employee_responses = {
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
    404: {
        'description': 'Not Found: Algum(ns) dos serviços informados não foi(foram) encontrado(s).',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 404,
                    'errors': {
                        'json': {
                            'service': ['Service not found.']
                        }
                    },
                    'status': 'Not Found'
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
                            'name': ['Email already registered.']
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
        '- `email`: o formato do email é inválido (deve ser um endereço de e-mail válido).\n'
        '- `service`: deve haver ao menos um serviço cadastrado antes de criar um funcionário(a).\n\n',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 422,
                    'errors': {
                        'json': {
                            'name': ['Missing data for required field.'],
                            'email': ['Missing data for required field.'],
                            'service': ['A service must be registered before registering an employee.']
                        }
                    },
                    'status': 'Unprocessable Entity'
                }
            }
        }
    }
}
