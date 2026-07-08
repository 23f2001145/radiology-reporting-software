from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date
from enum import Enum

class Gender(str, Enum):
    M = "M"
    F = "F"

class PatientCreate(BaseModel):
    patient_name: str
    dob: date
    gender: Gender

class PatientResponse(BaseModel):
    id: int
    patient_name: str
    dob: date
    gender : Gender
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class PatientUpdate(BaseModel):
    patient_name: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[Gender] = None

class PatientDelete(BaseModel):
    id: int