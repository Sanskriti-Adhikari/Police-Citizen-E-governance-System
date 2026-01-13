# backend/app/routers/auth.py
from fastapi import APIRouter, HTTPException, status, Depends
from datetime import timedelta

from app.schemas import Token, LoginRequest, User
from app.utils import authenticate_user, create_access_token, get_current_user
from app.database import fake_users_db
from app.schemas import UserRole, UserInDB

router = APIRouter()

# Helper to get user from fake DB
def get_user(username: str):
    if username in fake_users_db:
        return UserInDB(**fake_users_db[username])
    return None

@router.post("/login", response_model=Token)
async def login(login_data: LoginRequest):
    """Authenticate user and return JWT token"""
    user = authenticate_user(login_data.username, login_data.password, login_data.role, get_user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username, password, or role",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=480)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": User(**user.dict())
    }
