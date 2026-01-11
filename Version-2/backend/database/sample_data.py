from database.db import criminal_records_db, officers_db, record_id_counter, officer_id_counter
from datetime import datetime

def initialize_sample_data():
    global record_id_counter, officer_id_counter

    # Officers
    sample_officers = [
        {"id": 1, "name": "Officer Smith", "badge_id": "B001", "status": "Available", "area": "Downtown", "contact": "555-0101"},
        {"id": 2, "name": "Officer Johnson", "badge_id": "B002", "status": "On Duty", "area": "Northside", "contact": "555-0102"},
        {"id": 3, "name": "Officer Brown", "badge_id": "B003", "status": "On Leave", "area": "Eastside", "contact": "555-0103"},
    ]
    officers_db.extend(sample_officers)
    officer_id_counter = len(sample_officers) + 1

    # Criminal records
    sample_records = [
        {
            "id": 1,
            "criminal_name": "John Doe",
            "crime_type": "Theft",
            "severity": "Medium",
            "status": "Under Investigation",
            "location": "Downtown",
            "description": "Shoplifting at local store",
            "priority": 2,
            "officer_assigned": "Officer Smith",
            "created_at": datetime.now().isoformat(),
            "updated_at": None
        }
    ]
    criminal_records_db.extend(sample_records)
    record_id_counter = len(sample_records) + 1
