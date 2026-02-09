from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str 


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr]
    hashed_password: Optional[str]