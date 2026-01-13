# backend/app/routers/heatmap.py
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import User, UserRole
from app.database import crimes_db
from app.utils import get_current_user

router = APIRouter()

@router.get("/")
async def get_heatmap_data(current_user: User = Depends(get_current_user)):
    """Get crime heatmap data"""
    if current_user.role != UserRole.OFFICER:
        raise HTTPException(status_code=403, detail="Only officers can access heatmap data")
    
    return {
        "crimes": crimes_db,
        "statistics": {
            "total": len(crimes_db),
            "pending": len([c for c in crimes_db if c["status"] == "pending"]),
            "solved": len([c for c in crimes_db if c["status"] == "solved"]),
            "high_severity": len([c for c in crimes_db if c["severity"] == "High"])
        }
    }
