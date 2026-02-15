from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional
from core.deps import get_db 
from sqlalchemy.orm import sessionmaker, Session
from schemas.user import UserCreate, UserResponse, Token
from models.user import User
from core.security import get_pass_hash, verify_pass, create_access_token, TOKEN_EXPIRES
from datetime import timedelta


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=400,
            detail="Email already in use"
        )
    
    hashed_password = get_pass_hash(user.password)
    new_user = User(
        name= user.name,
        email= user.email,
        hashed_password= hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_pass(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=400,
            detail="Inactive user"
        )
    
    access_token_expires = timedelta(minutes=TOKEN_EXPIRES)
    access_token = create_access_token(
        data={"sub": user.email},
            expires_delta = access_token_expires
        )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }