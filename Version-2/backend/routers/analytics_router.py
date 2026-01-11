from fastapi import APIRouter
from models.analytics import AnalyticsResponse, HeatmapData, TrendData
from database.db import criminal_records_db, officers_db
from typing import List
import random

router = APIRouter(prefix="/api/analytics", tags=["Analytics"])

@router.get("/", response_model=AnalyticsResponse)
async def get_analytics():
    total_crimes = len(criminal_records_db)
    solved = len([r for r in criminal_records_db if r["status"] == "Solved"])
    pending = len([r for r in criminal_records_db if r["status"] == "Pending"])
    under_investigation = len([r for r in criminal_records_db if r["status"] == "Under Investigation"])
    total_officers = len(officers_db)
    available = len([o for o in officers_db if o["status"] == "Available"])
    on_duty = len([o for o in officers_db if o["status"] == "On Duty"])
    on_leave = len([o for o in officers_db if o["status"] == "On Leave"])
    return AnalyticsResponse(
        total_crimes=total_crimes,
        solved_cases=solved,
        pending_cases=pending,
        under_investigation=under_investigation,
        total_officers=total_officers,
        available_officers=available,
        on_duty_officers=on_duty,
        on_leave_officers=on_leave
    )

@router.get("/heatmap", response_model=List[HeatmapData])
async def get_heatmap():
    area_counts = {}
    for r in criminal_records_db:
        area_counts[r["location"]] = area_counts.get(r["location"], 0) + 1

    # Mock coordinates
    coords = {"Downtown": (27.7, 85.3), "Northside": (27.8, 85.3), "Eastside": (27.7, 85.4),
              "Westside": (27.7, 85.2), "Southside": (27.6, 85.3)}
    heatmap = []
    for area, count in area_counts.items():
        lat, lng = coords.get(area, (27.7, 85.3))
        heatmap.append({"area": area, "crimes": count, "lat": lat, "lng": lng})
    return sorted(heatmap, key=lambda x: x["crimes"], reverse=True)

@router.get("/trends", response_model=List[TrendData])
async def get_trends():
    months = ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
    trends = [{"month": m, "crimes": random.randint(10, 50)} for m in months]
    return trends
