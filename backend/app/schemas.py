# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

# Enums
class UserRole(str, Enum):
    OFFICER = "Officer"
    CITIZEN = "Citizen"

class CrimeStatus(str, Enum):
    PENDING = "pending"
    UNDER_INVESTIGATION = "under_investigation"
    SOLVED = "solved"
    CLOSED = "closed"

class ComplaintStatus(str, Enum):
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    SOLVED = "solved"
    CLOSED = "closed"

class Severity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class EmergencyType(str, Enum):
    CRIME = "Crime"
    MEDICAL = "Medical"
    ACCIDENT = "Accident"
    FIRE = "Fire"

# Pydantic Models
class User(BaseModel):
    id: str
    username: str
    role: UserRole
    full_name: Optional[str] = None
    badge_number: Optional[str] = None
    contact: Optional[str] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user: User

class LoginRequest(BaseModel):
    username: str
    password: str
    role: UserRole

class CrimeRecord(BaseModel):
    id: Optional[int] = None
    type: str
    lat: float
    lng: float
    severity: Severity
    date: str
    status: CrimeStatus
    description: str
    criminal_name: Optional[str] = None
    officer_assigned: Optional[str] = None
    evidence_files: Optional[List[str]] = []

class CriminalRecord(BaseModel):
    id: int
    name: str
    cases: int
    last_reported: str
    crime_history: List[str]
    photo: Optional[str] = None
    fingerprint_id: Optional[str] = None

class Complaint(BaseModel):
    id: Optional[int] = None
    citizen_id: str
    citizen_name: str
    type: str
    location: str
    description: str
    date: str
    status: ComplaintStatus
    priority: str = "low"
    anonymous: bool = False
    evidence: Optional[List[str]] = []
    officer_notes: Optional[str] = None

class EmergencyAlert(BaseModel):
    id: Optional[int] = None
    citizen_id: str
    type: EmergencyType
    location: str
    lat: float
    lng: float
    timestamp: str
    status: str = "dispatched"
    officer_assigned: Optional[str] = None
    anonymous: bool = False

class OfficerAllocation(BaseModel):
    id: str
    name: str
    badge: str
    status: str = "available"
    current_case: Optional[str] = None
    area: str
    assigned_crimes: Optional[int] = 0

class Notice(BaseModel):
    id: int
    title: str
    content: str
    category: str
    date: str
    priority: str = "normal"