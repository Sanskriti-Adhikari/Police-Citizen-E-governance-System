from pydantic import BaseModel
from typing import Optional

# ----------------- Criminal Records -----------------
class CriminalRecord(BaseModel):
    id: Optional[int] = None
    case_number: str
    name: str
    crime_type: str
    description: str
    location: str
    date_reported: str
    status: str  # Pending / Under Investigation / Solved
    assigned_officer: Optional[str] = None
    priority: Optional[int] = 0  # Officer-defined priority

# ----------------- Officer -----------------
class Officer(BaseModel):
    id: Optional[int] = None
    name: str
    badge_number: str
    rank: str
    status: str  # Available / On Duty / On Leave
    cases_assigned: int = 0
    area: Optional[str] = None
    holiday_dates: Optional[list] = []

# ----------------- Complaints -----------------
class Complaint(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    location: str
    is_anonymous: bool = False
    reporter_name: Optional[str] = None
    reporter_contact: Optional[str] = None
    status: str = "Pending"
    date_filed: Optional[str] = None
    tracking_id: Optional[str] = None
    evidence_files: Optional[list] = []  # Images/Videos

# ----------------- Emergency Alerts -----------------
class EmergencyAlert(BaseModel):
    id: Optional[int] = None
    type: str  # Crime / Medical / Accident / Fire
    location: str
    description: Optional[str] = None
    reporter_name: Optional[str] = None
    is_anonymous: bool = False
    priority_flag: Optional[bool] = True
    date_filed: Optional[str] = None