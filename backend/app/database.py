# backend/app/database.py
from app.schemas import UserRole

from app.config import pwd_context

# In-memory databases
fake_users_db = {
    "officer1": {
        "id": "off_001",
        "username": "officer1",
        "hashed_password": pwd_context.hash("password123"),
        "role": UserRole.OFFICER,
        "full_name": "Officer Sharma",
        "badge_number": "KTM-001",
        "contact": "9841234567"
    },
    "citizen1": {
        "id": "cit_001",
        "username": "citizen1",
        "hashed_password": pwd_context.hash("password123"),
        "role": UserRole.CITIZEN,
        "full_name": "John Doe",
        "contact": "9851234567"
    }
}

crimes_db = [
    {
        "id": 1,
        "type": "Theft",
        "lat": 27.7172,
        "lng": 85.3240,
        "severity": "Medium",
        "date": "2025-01-02",
        "status": "pending",
        "description": "Motorcycle theft reported",
        "criminal_name": None,
        "officer_assigned": "Officer Sharma"
    },
    {
        "id": 2,
        "type": "Assault",
        "lat": 27.7100,
        "lng": 85.3300,
        "severity": "High",
        "date": "2025-01-01",
        "status": "solved",
        "description": "Physical assault case",
        "criminal_name": "Ram Bahadur",
        "officer_assigned": "Officer Thapa"
    }
]

criminals_db = [
    {
        "id": 1,
        "name": "Ram Bahadur",
        "cases": 3,
        "last_reported": "2024-12-15",
        "crime_history": ["Theft", "Burglary", "Assault"],
        "photo": None,
        "fingerprint_id": "FP001"
    },
    {
        "id": 2,
        "name": "Shyam Kumar",
        "cases": 5,
        "last_reported": "2024-11-20",
        "crime_history": ["Theft", "Theft", "Vandalism", "Burglary", "Assault"],
        "photo": None,
        "fingerprint_id": "FP002"
    }
]

complaints_db = [
    {
        "id": 1,
        "citizen_id": "cit_001",
        "citizen_name": "John Doe",
        "type": "Noise Complaint",
        "location": "Thamel",
        "description": "Loud music at night",
        "date": "2025-01-02",
        "status": "submitted",
        "priority": "low",
        "anonymous": False
    }
]

officers_db = [
    {
        "id": "off_001",
        "name": "Officer Sharma",
        "badge": "KTM-001",
        "status": "available",
        "current_case": None,
        "area": "Thamel",
        "assigned_crimes": 0
    },
    {
        "id": "off_002",
        "name": "Officer Thapa",
        "badge": "KTM-002",
        "status": "busy",
        "current_case": "Case #123",
        "area": "Patan",
        "assigned_crimes": 2
    }
]

notices_db = [
    {
        "id": 1,
        "title": "Traffic Restrictions",
        "content": "Traffic restrictions in Thamel area from Jan 5-7 due to public event.",
        "category": "Public Notice",
        "date": "2025-01-02",
        "priority": "high"
    }
]