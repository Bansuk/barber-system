"""
Validation module for Appointment entities.
"""

from datetime import datetime
from validations.validation_error import ValidationError


class AppointmentValidation():
    """
    Validation class for Employee entities.

    Extends UserValidation and adds additional checks, such as
    verifying whether an email is already registered in the Employee table.
    """

    # validade da data
    # nao pode ser antes que agora e nao pode ser mais de um mes de antecedencia
    # usuario e funcionario nao podem ter o horario ja reservado
    # working hours
    # tem que ter customer registrado
    # tem que ter employee registrado
    # tem que ter service registrado

    @staticmethod
    def _are_inputs_valid(date: datetime, customer_id: int,
                          employee_id: int, services_ids: list[int]) -> bool:
        """
        Validates that all required inputs are provided.

        Args:
            date (datetime): The appointment date.
            customer_id (int): The customer's ID.
            employee_id (int): The employee's ID.
            services_ids (list[int]): List of service IDs.

        Returns:
            bool: True if all inputs are valid, False otherwise.
        """

        print(date, customer_id, employee_id, services_ids)

        return all([date, customer_id, employee_id, services_ids])

    @staticmethod
    def validate_appointment_data(date: datetime, customer_id: int,
                                  employee_id: int, services_ids: list[int]):
        """
        Validates appointment data.

        Args:
            date (datetime): The appointment date.
            customer_id (int): The customer's ID.
            employee_id (int): The employee's ID.
            services_ids (list[int]): List of service IDs.

        Raises:
            ValidationError: If provided email already exists.
        """

        if not AppointmentValidation._are_inputs_valid(date, customer_id, employee_id, services_ids):
            raise ValidationError({'input': 'Parametros insuficientes.'})
