from pydantic import BaseModel
from typing import List

class AnalyticsResponse(BaseModel):
    total_crimes: int
    solved_cases: int
    pending_cases: int
    under_investigation: int
    total_officers: int
    available_officers: int
    on_duty_officers: int
    on_leave_officers: int

class HeatmapData(BaseModel):
    area: str
    crimes: int
    lat: float
    lng: float

class TrendData(BaseModel):
    month: str
    crimes: int
