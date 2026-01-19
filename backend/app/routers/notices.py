# backend/app/routers/notices.py
from fastapi import APIRouter
from typing import List
from app.schemas import Notice
from app.database import notices_db

router = APIRouter()

@router.get("/", response_model=List[Notice])
async def get_notices():
    """Get public notices and information"""
    return notices_db
