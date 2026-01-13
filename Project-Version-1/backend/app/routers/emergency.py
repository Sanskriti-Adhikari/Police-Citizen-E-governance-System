# backend/app/routers/emergency.py
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from typing import Dict

from app.schemas import EmergencyAlert, User, UserRole
from app.database import officers_db
from app.utils import get_current_user

router = APIRouter()

@router.post("/", response_model=Dict)
async def create_emergency_alert(alert: EmergencyAlert, current_user: User = Depends(get_current_user)):
    """Send emergency alert"""
    if current_user.role != UserRole.CITIZEN:
        raise HTTPException(status_code=403, detail="Only citizens can send emergency alerts")
    
    alert_dict = alert.dict()
    alert_dict["id"] = int(datetime.now().timestamp())
    alert_dict["citizen_id"] = current_user.id
    alert_dict["timestamp"] = datetime.now().isoformat()
    alert_dict["status"] = "dispatched"
    
    # Find nearest available officer
    available_officers = [o for o in officers_db if o["status"] == "available"]
    if available_officers:
        alert_dict["officer_assigned"] = available_officers[0]["name"]
        available_officers[0]["status"] = "responding"
        available_officers[0]["current_case"] = f"Emergency Alert #{alert_dict['id']}"
    
    return {
        "success": True,
        "alert_id": alert_dict["id"],
        "message": "Emergency alert dispatched",
        "officer_assigned": alert_dict.get("officer_assigned"),
        "estimated_arrival": "5-10 minutes"
    }
