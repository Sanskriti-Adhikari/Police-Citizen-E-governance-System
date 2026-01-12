from pydantic import BaseModel
from datetime import datetime

class HolidayRequest(BaseModel):
    officer_id: int
    start_date: datetime
    end_date: datetime
    reason: str

class HolidayResponse(BaseModel):
    id: int
    officer_id: int
    officer_name: str
    start_date: datetime
    end_date: datetime
    reason: str
    status: str
    created_at: datetime

class DutyRotation(BaseModel):
    officer_id: int
    officer_name: str
    area: str
    shift: str
    date: datetime
