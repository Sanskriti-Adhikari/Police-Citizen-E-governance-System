from fastapi import APIRouter, HTTPException
from models.holiday import HolidayRequest, HolidayResponse
from database.db import holiday_requests_db, officers_db, holiday_id_counter
from datetime import datetime

router = APIRouter(prefix="/api/holidays", tags=["Holiday Management"])

@router.post("/request", response_model=HolidayResponse)
async def request_holiday(req: HolidayRequest):
    global holiday_id_counter
    officer = next((o for o in officers_db if o["id"] == req.officer_id), None)
    if not officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    if req.end_date <= req.start_date:
        raise HTTPException(status_code=400, detail="End date must be after start date")
    new_holiday = {
        "id": holiday_id_counter,
        "officer_id": req.officer_id,
        "officer_name": officer["name"],
        "start_date": req.start_date.isoformat(),
        "end_date": req.end_date.isoformat(),
        "reason": req.reason,
        "status": "Pending",
        "created_at": datetime.now().isoformat()
    }
    holiday_requests_db.append(new_holiday)
    holiday_id_counter += 1
    return new_holiday

@router.get("/", response_model=list[HolidayResponse])
async def list_holidays():
    return holiday_requests_db
