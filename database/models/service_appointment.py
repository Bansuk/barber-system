"""
This module defines the many-to-many association table between Service and Appointment.
"""

from database.db_setup import db

service_appointment = db.Table(
    'service_appointment',
    db.Column('service_id', db.Integer, db.ForeignKey(
        'service.id'), primary_key=True),
    db.Column('appointment_id', db.Integer, db.ForeignKey(
        'appointment.id'), primary_key=True)
)
