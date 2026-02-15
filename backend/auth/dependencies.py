from fastapi import Depends, HTTPException, status
from models.user import User
from core.security import verify_token, oauth2_scheme
from sqlalchemy.orm import sessionmaker, Session
from core.deps import get_db


def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_token(token)
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User does not exist",
                headers={"WWW-Authenticate":"Bearer"}
            )
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(
            status_code=404,
            detail="Inactive user",
        )
    return current_user