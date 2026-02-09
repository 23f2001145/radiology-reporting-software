from fastapi import APIRouter, HTTPException, Depends, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional
from datetime import datetime, timedelta
import jwt
from core.deps import get_db 
from sqlalchemy.orm import sessionmaker, Session
from models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
TOKEN_EXPIRES = 30
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_pass(plain_pass: str, hashed_pass: str) ->bool:
    return pwd_context.verify(plain_pass, hashed_pass)

def get_pass_hash(password:str) -> str:
    return pwd_context.hash(password)

def create_access_token(data:dict, expires_delta:Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not verify credentials",
                headers={"WWW-Authenticate":"Bearer"}
            )
        return token
    except jwt.PyJWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not verify credentials",
                headers={"WWW-Authenticate":"Bearer"}
            )

def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_token(token)
    user = db.query(User).filer(User.email == token_data.email).first()
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User does not exist",
                headers={"WWW-Authenticate":"Bearer"}
            )

@router.post("/register")
def register_user(db: Session = Depends(get_db)):
    return {"register": "working"}