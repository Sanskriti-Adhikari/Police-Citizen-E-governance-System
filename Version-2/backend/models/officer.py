from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class OfficerStatus(str, Enum):
    AVAILABLE = "Available"
    ON_DUTY = "On Duty"
    ON_LEAVE = "On Leave"

class OfficerBase(BaseModel):
    name: str
    badge_id: str
    status: OfficerStatus
    area: str
    contact: str

class OfficerCreate(OfficerBase):
    pass

class OfficerUpdate(BaseModel):
    name: Optional[str]
    badge_id: Optional[str]
    status: Optional[OfficerStatus]
    area: Optional[str]
    contact: Optional[str]

class Officer(OfficerBase):
    id: int
