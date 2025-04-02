"""
This module defines the many-to-many association table between Service and Employee.
"""

from database.db_setup import db

service_employee = db.Table(
    'service_employee',
    db.Column('service_id', db.Integer, db.ForeignKey(
        'service.id'), primary_key=True),
    db.Column('employee_id', db.Integer, db.ForeignKey(
        'employee.id'), primary_key=True)
)
