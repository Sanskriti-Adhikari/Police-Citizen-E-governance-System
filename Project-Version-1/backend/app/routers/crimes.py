# backend/app/routers/crimes.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from datetime import datetime

from app.schemas import CrimeRecord, User, UserRole
from app.database import crimes_db
from app.utils import get_current_user

router = APIRouter()

@router.get("/", response_model=List[CrimeRecord])
async def get_crimes(
    current_user: User = Depends(get_current_user),
    status: Optional[str] = None,
    crime_type: Optional[str] = None,
    severity: Optional[str] = None
):
    filtered_crimes = crimes_db.copy()
    if status and status != "all":
        filtered_crimes = [c for c in filtered_crimes if c["status"] == status]
    if crime_type and crime_type != "all":
        filtered_crimes = [c for c in filtered_crimes if c["type"] == crime_type]
    if severity and severity != "all":
        filtered_crimes = [c for c in filtered_crimes if c["severity"] == severity]
    return filtered_crimes

@router.post("/", response_model=CrimeRecord)
async def create_crime_record(crime: CrimeRecord, current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can create crime records")
    crime_dict = crime.dict()
    crime_dict["id"] = len(crimes_db) + 1
    crime_dict["date"] = datetime.now().strftime("%Y-%m-%d")
    crimes_db.append(crime_dict)
    return crime_dict

@router.put("/{crime_id}", response_model=CrimeRecord)
async def update_crime_record(crime_id: int, crime: CrimeRecord, current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can update crime records")
    for idx, c in enumerate(crimes_db):
        if c["id"] == crime_id:
            crime_dict = crime.dict()
            crime_dict["id"] = crime_id
            crimes_db[idx] = crime_dict
            return crime_dict
    raise HTTPException(status_code=404, detail="Crime record not found")
