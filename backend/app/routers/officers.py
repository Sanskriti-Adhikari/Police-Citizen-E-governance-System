# backend/app/routers/officers.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas import OfficerAllocation, User, UserRole
from app.database import officers_db, crimes_db
from app.utils import get_current_user

router = APIRouter()

@router.get("/", response_model=List[OfficerAllocation])
async def get_officers(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can view officer data")
    return officers_db

@router.post("/allocate", response_model=List[OfficerAllocation])
async def allocate_officers(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can allocate resources")
    
    # Calculate crime density by area
    crime_by_area = {}
    for crime in crimes_db:
        if crime["status"] == "pending":
            area = "North" if crime["lat"] > 27.715 else "South"
            crime_by_area[area] = crime_by_area.get(area, 0) + 1
    
    available_officers = [o for o in officers_db if o["status"] == "available"]
    for idx, officer in enumerate(available_officers):
        area = list(crime_by_area.keys())[idx % len(crime_by_area)] if crime_by_area else "Central"
        officer["area"] = area
        officer["assigned_crimes"] = crime_by_area.get(area, 0)
    
    return officers_db
