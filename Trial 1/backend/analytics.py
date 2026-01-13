from fastapi import APIRouter
from typing import Dict

router = APIRouter()

# Needs criminal_records and officers from main or import
def generate_analytics(criminal_records, officers):
    total_cases = len(criminal_records)
    pending = len([r for r in criminal_records if r["status"]=="Pending"])
    solved = len([r for r in criminal_records if r["status"]=="Solved"])

    crime_by_type = {}
    for r in criminal_records:
        crime_by_type[r["crime_type"]] = crime_by_type.get(r["crime_type"], 0)+1

    available_officers = len([o for o in officers if o["status"]=="Available"])

    return {
        "total_cases": total_cases,
        "pending": pending,
        "solved": solved,
        "crime_by_type": crime_by_type,
        "available_officers": available_officers
    }

@router.get("/analytics")
def get_analytics(criminal_records: list, officers: list):
    return generate_analytics(criminal_records, officers)