from fastapi import APIRouter, HTTPException
from typing import List
from models.criminal import CriminalRecord, CriminalRecordCreate, CriminalRecordUpdate
from crud.criminal_crud import get_all_records, get_record, create_record, update_record, delete_record
from utils.notifications import create_notification
from models.criminal import CaseStatus

router = APIRouter(prefix="/api/records", tags=["Criminal Records"])

@router.get("/", response_model=List[CriminalRecord])
async def read_records():
    return get_all_records()

@router.get("/{record_id}", response_model=CriminalRecord)
async def read_record(record_id: int):
    record = get_record(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@router.post("/", response_model=CriminalRecord)
async def add_record(record: CriminalRecordCreate):
    return create_record(record)

@router.put("/{record_id}", response_model=CriminalRecord)
async def edit_record(record_id: int, record_update: CriminalRecordUpdate):
    record = update_record(record_id, record_update)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    # Notify if solved
    if record_update.status == CaseStatus.SOLVED:
        create_notification(record_id, "Case solved", "case_solved")
    return record

@router.delete("/{record_id}")
async def remove_record(record_id: int):
    delete_record(record_id)
    return {"message": "Record deleted"}
