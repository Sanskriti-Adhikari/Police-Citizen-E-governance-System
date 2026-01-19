# backend/app/routers/upload.py
from fastapi import APIRouter, UploadFile, File, Depends
from app.schemas import User
from app.utils import get_current_user

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    """Upload evidence file"""
    return {
        "success": True,
        "filename": file.filename,
        "url": f"/uploads/{file.filename}",
        "message": "File uploaded successfully"
    }
