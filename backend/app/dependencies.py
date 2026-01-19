# app/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from .config import SECRET_KEY, ALGORITHM
from .models import User
from .database import fake_users_db

security = HTTPBearer()

def get_user(username: str):
    user = fake_users_db.get(username)
    if user:
        return user
    return None

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = get_user(username)
        if user is None:
            raise credentials_exception
        return User(**user.dict())
    except JWTError:
        raise credentials_exception
