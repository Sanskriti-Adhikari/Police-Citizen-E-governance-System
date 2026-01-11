from fastapi import APIRouter, HTTPException
from models.allocation import AllocationRequest, AllocationResponse, AllocationResult
from database.db import criminal_records_db
from typing import List

router = APIRouter(prefix="/api/allocation", tags=["Officer Allocation"])

@router.post("/allocate", response_model=AllocationResponse)
async def allocate_officers(req: AllocationRequest):
    total_officers = req.total_officers
    area_crimes = {}
    for r in criminal_records_db:
        area_crimes[r["location"]] = area_crimes.get(r["location"], 0) + 1
    if not area_crimes:
        raise HTTPException(status_code=400, detail="No crime data available")
    total_crimes = sum(area_crimes.values())

    allocation: List[AllocationResult] = []
    allocated_count = 0
    for area, crimes in sorted(area_crimes.items(), key=lambda x: x[1], reverse=True):
        proportion = crimes / total_crimes
        officers_needed = max(1, round(proportion * total_officers))
        allocation.append(AllocationResult(area=area, officers=officers_needed, crime_rate=crimes))
        allocated_count += officers_needed

    # Adjust difference
    diff = total_officers - allocated_count
    if diff != 0:
        allocation[0].officers += diff

    high_crime_areas = [a.area for a in allocation if a.crime_rate > total_crimes / len(area_crimes)]
    recommendation = f"High crime in {', '.join(high_crime_areas)}" if high_crime_areas else "Crime balanced"
    return AllocationResponse(allocation=allocation, total_allocated=total_officers, recommendation=recommendation)
