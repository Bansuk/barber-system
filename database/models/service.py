from datetime import datetime
from database.db_setup import db


class Service(db.Model):
    """
    Represents a service entity in the database.

    Attributes:
        id (int): Primary key identifier.
        name (str): Name of the service.
        price (int): Price of the service.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price
