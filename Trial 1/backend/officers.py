from fastapi import APIRouter, HTTPException
from models import Officer
from typing import List

router = APIRouter()
officers: List[dict] = []

#----------------- Officer CRUD -----------------
@router.get("/officers")
def get_officers():
    return officers

@router.post("/officers")
def create_officer(officer: Officer):
    new_id = max([o["id"] for o in officers], default=0) + 1
    new_officer = officer.dict()
    new_officer["id"] = new_id
    officers.append(new_officer)
    return new_officer

@router.put("/officers/{officer_id}")
def update_officer(officer_id: int, officer: Officer):
    for i, o in enumerate(officers):
        if o["id"] == officer_id:
            officers[i] = officer.dict()
            officers[i]["id"] = officer_id
            return officers[i]
    raise HTTPException(status_code=404, detail="Officer not found")

#----------------- Simple Allocation Logic -----------------
def auto_allocate_officer(area: str):
    # Returns an available officer in the area or None
    for o in officers:
        if o["status"] == "Available" and (o.get("area") == area or not o.get("area")):
            o["cases_assigned"] += 1
            return o["name"]
    return None