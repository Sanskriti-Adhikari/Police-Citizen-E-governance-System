from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NotificationCreate(BaseModel):
    case_id: int
    citizen_id: Optional[int] = None
    message: str
    notification_type: str

class Notification(BaseModel):
    id: int
    case_id: int
    citizen_id: Optional[int]
    message: str
    notification_type: str
    created_at: datetime
    read: bool = False
