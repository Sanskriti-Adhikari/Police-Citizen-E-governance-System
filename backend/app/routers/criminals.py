# backend/app/routers/criminals.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional

from app.schemas import CriminalRecord, User, UserRole
from app.database import criminals_db
from app.utils import get_current_user

router = APIRouter()

@router.get("/", response_model=List[CriminalRecord])
async def get_criminals(current_user: User = Depends(get_current_user), name: Optional[str] = None):
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can access criminal records")
    if name:
        return [c for c in criminals_db if name.lower() in c["name"].lower()]
    return criminals_db

@router.get("/{criminal_id}", response_model=CriminalRecord)
async def get_criminal(criminal_id: int, current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can access criminal records")
    for criminal in criminals_db:
        if criminal["id"] == criminal_id:
            return criminal
    raise HTTPException(status_code=404, detail="Criminal not found")
