from fastapi import APIRouter, HTTPException
from models import Complaint
from datetime import datetime
import random
from typing import List

router = APIRouter()
complaints: List[dict] = []

def generate_tracking_id():
    return f"TRACK{random.randint(100000,999999)}"

@router.post("/complaints")
def file_complaint(complaint: Complaint):
    new_id = max([c["id"] for c in complaints], default=0) + 1
    tracking_id = generate_tracking_id()
    new_complaint = complaint.dict()
    new_complaint.update({
        "id": new_id,
        "tracking_id": tracking_id,
        "status": "Pending",
        "date_filed": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "reporter_name": "Anonymous" if complaint.is_anonymous else complaint.reporter_name
    })
    complaints.append(new_complaint)
    return new_complaint

@router.get("/complaints")
def get_complaints():
    return complaints

@router.get("/complaints/track/{tracking_id}")
def track_complaint(tracking_id: str):
    complaint = next((c for c in complaints if c["tracking_id"] == tracking_id), None)
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return complaint
