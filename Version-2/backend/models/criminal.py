from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class Severity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class CaseStatus(str, Enum):
    PENDING = "Pending"
    UNDER_INVESTIGATION = "Under Investigation"
    SOLVED = "Solved"

class CriminalRecordBase(BaseModel):
    criminal_name: str = Field(..., min_length=1, max_length=200)
    crime_type: str
    severity: Severity
    status: CaseStatus
    location: str
    description: Optional[str] = None
    priority: int = Field(..., ge=1, le=5)
    officer_assigned: Optional[str] = None

class CriminalRecordCreate(CriminalRecordBase):
    pass

class CriminalRecordUpdate(BaseModel):
    criminal_name: Optional[str]
    crime_type: Optional[str]
    severity: Optional[Severity]
    status: Optional[CaseStatus]
    location: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    officer_assigned: Optional[str]

class CriminalRecord(CriminalRecordBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
