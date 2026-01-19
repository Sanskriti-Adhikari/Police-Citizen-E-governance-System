# backend/app/routers/complaints.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
from datetime import datetime

from app.schemas import Complaint, User, UserRole
from app.database import complaints_db
from app.utils import get_current_user, validate_complaint

router = APIRouter()

@router.get("/", response_model=List[Complaint])
async def get_complaints(current_user: User = Depends(get_current_user)):
    if current_user.role == UserRole.OFFICER:
        return complaints_db
    else:
        return [c for c in complaints_db if c["citizen_id"] == current_user.id]

@router.post("/", response_model=Dict)
async def create_complaint(complaint: Complaint, current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.CITIZEN:
        raise HTTPException(status_code=403, detail="Only citizens can file complaints")
    validation = validate_complaint(complaint)
    if not validation["valid"]:
        raise HTTPException(status_code=400, detail=f"Invalid complaint: {', '.join(validation['issues'])}")
    complaint_dict = complaint.dict()
    complaint_dict["id"] = len(complaints_db) + 1
    complaint_dict["citizen_id"] = current_user.id
    complaint_dict["citizen_name"] = current_user.full_name or current_user.username
    complaint_dict["date"] = datetime.now().strftime("%Y-%m-%d")
    complaint_dict["status"] = "submitted"
    high_priority_keywords = ["emergency", "urgent", "violence", "theft", "assault"]
    if any(keyword in complaint.description.lower() for keyword in high_priority_keywords):
        complaint_dict["priority"] = "high"
    complaints_db.append(complaint_dict)
    return {
        "success": True,
        "complaint_id": complaint_dict["id"],
        "message": "Complaint filed successfully",
        "validation_score": validation["score"]
    }

@router.put("/{complaint_id}", response_model=Complaint)
async def update_complaint(complaint_id: int, updates: Dict, current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can update complaints")
    for idx, complaint in enumerate(complaints_db):
        if complaint["id"] == complaint_id:
            complaints_db[idx].update(updates)
            return complaints_db[idx]
    raise HTTPException(status_code=404, detail="Complaint not found")
