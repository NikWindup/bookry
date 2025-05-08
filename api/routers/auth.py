from fastapi import APIRouter, HTTPException, Depends, status
from datetime import datetime, timedelta
from typing import Optional
import jwt
from pydantic import BaseModel, EmailStr

from schemas.User import User, UserCreate, UserLogin, UserResponse
from core.auth import create_access_token, get_current_user
from core.config import settings
from dao.UserDao import UserDao
from dao.HashDao import HashDao
from dao.SaltDao import SaltDao

router = APIRouter(prefix="/auth", tags=["auth"])

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/register", response_model=Token)
async def register_user(user: UserCreate):
    try:
        if UserDao.select_by_email(email=user.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        user_db = UserDao.insert(user.email, user.username)
        salt = SaltDao.insert(user_id=user_db.id)
        HashDao.insert(user_id=user_db.id, password=user.password, salt=salt)
        
        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/login", response_model=Token)
async def login_user(user: UserLogin):
    try:
        user_db = UserDao.select_by_email(email=user.email)
        if not user_db:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        
        hash = HashDao.select_by_user_id(user_id=user_db.id)
        salt = SaltDao.select_by_user_id(user_id=user_db.id)
        
        if not hash or HashDao.hash(password=user.password, salt=salt) != hash:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        
        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user 