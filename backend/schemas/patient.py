from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

class Gender(Enum):
    M = 'M'
    F = 'F'

class PatientCreate(BaseModel):
    patient_name: str
    dob: date
    gender: Gender

class UpdatePatient(BaseModel):
    patient_name: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[Gender] = None