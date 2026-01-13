from fastapi import APIRouter
from models import EmergencyAlert
from datetime import datetime

router = APIRouter()
emergencies = []

@router.post("/emergency")
def send_alert(alert: EmergencyAlert):
    new_id = len(emergencies) + 1
    new_alert = alert.dict()
    new_alert.update({"id": new_id, "date_filed": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    emergencies.append(new_alert)
    return {"alert": new_alert, "message": "Alert sent to nearest police unit"}
