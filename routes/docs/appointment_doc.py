"""
This module contains standard descriptions and responses for the Appointment API.
"""

from schemas.error_schema import ErrorSchema


GET_APPOINTMENT_SUMMARY = 'Retorna a lista de todos os agendamentos cadatrados.'
GET_APPOINTMENT_DESCRIPTION = 'Este endpoint retorna uma coleção de agendamentos cadastrados ' \
    'no formato JSON.'
POST_APPOINTMENT_SUMMARY = 'Lida com a criação de um novo agendamento.'
POST_APPOINTMENT_DESCRIPTION = 'Este endpoint processa o envio de um formulário (JSON) ' \
    'para criar um novo registro de agendamento.'
appointment_responses = {
    400: {
        'description':
        'Bad Request: A requisição está fora dos parâmetros adequados.\n\n'
        '**Motivos Possíveis:**\n'
        '- `json`: O formato do corpo JSON é inválido.\n'
        '- `date`: A data selecionada está fora do intervalo permitido.\n'
        '- `date`: O horário selecionado está fora do intervalo permitido.\n\n',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': [
                    {
                        'code': 400,
                        'errors': {
                            'json': [
                                'Invalid JSON body.'
                            ]
                        },
                        'status': 'Bad Request'
                    },
                    {
                        'code': 400,
                        'errors': {
                            'json': {
                                'date': [
                                    'Date is outside of allowed range.',
                                    'Hour is outside of working hours.'
                                ]
                            }
                        },
                        'status': 'Bad Request'
                    }
                ]
            }
        }
    },
    404: {
        'description':
        'Not Found: Serviços e/ou cliente e/ou funcionário(a) informados não foram encontrados.',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 404,
                    'errors': {
                        'json': {
                            'service': ['Provided services were not found.'],
                            'employee': ['Provided employee was not found.'],
                            'customer': ['Provided customer was not found.']
                        }
                    },
                    'status': 'Not Found'
                }
            }
        }
    },
    409: {
        'description': 'Conflict: O horário selecionado já está ocupado.',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 409,
                    'errors': {
                        'json': {
                            'date': ['Selecetd date is unavailable.']}
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
        '- `date` é obrigatório, mas não foi fornecido.\n'
        '- `customer_id` é obrigatório, mas não foi fornecido.\n'
        '- `employee_id` é obrigatório, mas não foi fornecido.\n'
        '- `services_ids` é obrigatório, mas não foi fornecido.\n\n',
        'content': {
            'application/json': {
                'schema': ErrorSchema,
                'example': {
                    'code': 422,
                    'errors': {
                        'json': {
                            'date': ['Missing data for required field.'],
                            'customer_id': ['Missing data for required field.'],
                            'employee_id': ['Missing data for required field.'],
                            'services_ids': ['Missing data for required field.',
                                             "Length must be between 1 and 10."]
                        }
                    },
                    'status': 'Unprocessable Entity'
                }
            }
        }
    }
}
