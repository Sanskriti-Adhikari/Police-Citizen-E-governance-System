from fastapi import APIRouter, HTTPException
from models import CriminalRecord
from typing import List

router = APIRouter()
criminal_records: List[dict] = []

# ----------------- Helpers -----------------
def check_duplicate_record(name: str, crime_type: str) -> bool:
    for record in criminal_records:
        if record["name"].lower() == name.lower() and record["crime_type"].lower() == crime_type.lower():
            return True
    return False

def get_past_records(name: str) -> List[dict]:
    return [r for r in criminal_records if r["name"].lower() == name.lower()]

# ----------------- Routes -----------------
@router.get("/records")
def get_records():
    return criminal_records

@router.get("/records/{record_id}")
def get_record(record_id: int):
    record = next((r for r in criminal_records if r["id"] == record_id), None)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@router.post("/records")
def create_record(record: CriminalRecord):
    new_id = max([r["id"] for r in criminal_records], default=0) + 1
    new_record = record.dict()
    new_record["id"] = new_id
    criminal_records.append(new_record)
    
    # Smart side panel
    past_records = get_past_records(record.name)
    return {
        "record": new_record,
        "duplicate": len(past_records) > 1,
        "past_records": past_records
    }

@router.put("/records/{record_id}")
def update_record(record_id: int, record: CriminalRecord):
    for i, r in enumerate(criminal_records):
        if r["id"] == record_id:
            criminal_records[i] = record.dict()
            criminal_records[i]["id"] = record_id
            return criminal_records[i]
    raise HTTPException(status_code=404, detail="Record not found")

@router.delete("/records/{record_id}")
def delete_record(record_id: int):
    for i, r in enumerate(criminal_records):
        if r["id"] == record_id:
            return {"deleted": criminal_records.pop(i)}
    raise HTTPException(status_code=404, detail="Record not found")
