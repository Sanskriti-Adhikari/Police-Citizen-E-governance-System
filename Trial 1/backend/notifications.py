from fastapi import APIRouter
from typing import List

router = APIRouter()
notifications: List[dict] = []

def notify_citizen(tracking_id: str, status: str):
    notifications.append({"tracking_id": tracking_id, "status": status})
    return {"tracking_id": tracking_id, "status": status, "message": "Citizen notified"}

@router.get("/notifications")
def get_notifications():
    return notifications