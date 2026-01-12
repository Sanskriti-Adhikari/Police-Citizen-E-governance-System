from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.officer import Officer, OfficerCreate, OfficerUpdate, OfficerStatus
from crud.officer_crud import get_all_officers, get_officer, create_officer, update_officer, delete_officer

router = APIRouter(prefix="/api/officers", tags=["Officers"])

@router.get("/", response_model=List[Officer])
async def read_officers(status: Optional[OfficerStatus] = None, area: Optional[str] = None):
    officers = get_all_officers()
    if status:
        officers = [o for o in officers if o["status"] == status.value]
    if area:
        officers = [o for o in officers if o["area"].lower() == area.lower()]
    return officers

@router.get("/{officer_id}", response_model=Officer)
async def read_officer(officer_id: int):
    officer = get_officer(officer_id)
    if not officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return officer

@router.post("/", response_model=Officer)
async def add_officer(officer: OfficerCreate):
    # Check duplicate badge
    if any(o["badge_id"] == officer.badge_id for o in get_all_officers()):
        raise HTTPException(status_code=400, detail="Badge ID already exists")
    return create_officer(officer)

@router.put("/{officer_id}", response_model=Officer)
async def edit_officer(officer_id: int, officer_update: OfficerUpdate):
    officer = update_officer(officer_id, officer_update)
    if not officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return officer

@router.delete("/{officer_id}")
async def remove_officer(officer_id: int):
    delete_officer(officer_id)
    return {"message": "Officer deleted"}
