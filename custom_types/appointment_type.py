from typing import List, TypedDict

class AppointmentData(TypedDict):
    date: str
    customer_id: int
    employee_id: int
    services_ids: List[int]
