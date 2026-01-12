from database.db import criminal_records_db, record_id_counter
from models.criminal import CriminalRecordCreate, CriminalRecordUpdate, CaseStatus
from datetime import datetime

def get_all_records():
    return criminal_records_db

def get_record(record_id: int):
    return next((r for r in criminal_records_db if r["id"] == record_id), None)

def create_record(record: CriminalRecordCreate):
    global record_id_counter
    new_record = record.dict()
    new_record["id"] = record_id_counter
    new_record["created_at"] = datetime.now().isoformat()
    new_record["updated_at"] = None
    criminal_records_db.append(new_record)
    record_id_counter += 1
    return new_record

def update_record(record_id: int, record_update: CriminalRecordUpdate):
    record = get_record(record_id)
    if not record:
        return None
    update_data = record_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        record[key] = value
    record["updated_at"] = datetime.now().isoformat()
    return record

def delete_record(record_id: int):
    global criminal_records_db
    criminal_records_db = [r for r in criminal_records_db if r["id"] != record_id]
