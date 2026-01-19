# backend/app/utils.py
from app.config import pwd_context, SECRET_KEY, ALGORITHM
from app.schemas import UserInDB, Complaint, UserRole
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError

security = HTTPBearer()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def validate_complaint(complaint: Complaint) -> dict:
    validation_score = 100
    issues = []
    
    if len(complaint.description) < 20:
        validation_score -= 30
        issues.append("Description too short")
    
    if not complaint.location or len(complaint.location) < 3:
        validation_score -= 20
        issues.append("Invalid location")
    
    spam_keywords = ["test", "fake", "spam", "asdf"]
    if any(keyword in complaint.description.lower() for keyword in spam_keywords):
        validation_score -= 50
        issues.append("Potential spam detected")
    
    return {
        "valid": validation_score >= 50,
        "score": validation_score,
        "issues": issues
    }

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), get_user_func=None):
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
        user = get_user_func(username)
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception

def authenticate_user(username: str, password: str, role: UserRole, get_user_func):
    user = get_user_func(username)
    if not user or not verify_password(password, user.hashed_password) or user.role != role:
        return False
    return user