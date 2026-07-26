from fastapi import APIRouter, Depends, status, HTTPException
from schemas.patient import PatientCreate, PatientResponse, PatientUpdate
from sqlalchemy.orm import Session
from core.deps import get_db
from auth.dependencies import get_current_active_user
from models import User, Patient
from datetime import date

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    
    if(not patient.patient_name.strip()):
        raise HTTPException(
            status_code=400,
            detail="Patient name cannot be empty"
        )
    
    if(patient.dob > date.today()):
        raise HTTPException(
            status_code=400,
            detail="Date of birth cannot be in the future"
        )

    new_patient = Patient(
        patient_name= patient.patient_name,
        dob= patient.dob,
        gender= patient.gender,
        user_id= current_user.id
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


@router.get("/{patient_id}", response_model=PatientResponse, status_code=status.HTTP_200_OK)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    patient = (
        db.query(Patient)
        .filter(
            Patient.id == patient_id,
            Patient.user_id == current_user.id,
            Patient.is_active == True,
        )
        .first()
    )

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    return patient


@router.patch("/{patient_id}", response_model=PatientResponse, status_code=status.HTTP_200_OK)
def update_patient(patient_id : int, patient : PatientUpdate, db : Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):
    
    if(patient.patient_name is not None and not patient.patient_name.strip()):
        raise HTTPException(
            status_code=400,
            detail="Patient name cannot be empty"
        )
    
    if(patient.dob and patient.dob > date.today()):
        raise HTTPException(
            status_code=400,
            detail="Date of birth cannot be in the future"
        )
    
    existing_patient = db.query(Patient).filter(Patient.id == patient_id, Patient.user_id == current_user.id, Patient.is_active == True).first()

    if not existing_patient:
        raise HTTPException(
            status_code=404,
            detail="No such patient found"
        )

    if patient.patient_name is not None:
        existing_patient.patient_name = patient.patient_name

    if patient.dob is not None:
        existing_patient.dob = patient.dob

    if patient.gender is not None:
        existing_patient.gender = patient.gender

    db.commit()
    db.refresh(existing_patient)
    return existing_patient


@router.patch("/{patient_id}/deactivate", status_code=status.HTTP_200_OK)
def deactivate_patient(patient_id : int, db : Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):
    patient = db.query(Patient).filter(Patient.id == patient_id, Patient.user_id == current_user.id, Patient.is_active == True).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="No such patient found"
        )

    patient.is_active = False
    # db.delete(patient)
    db.commit()

    return {"msg": "Patient deactivated successfully"}

@router.get("/", response_model=list[PatientResponse], status_code=status.HTTP_200_OK)
def list_all_patients(db : Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):
    patients = db.query(Patient).filter(Patient.user_id == current_user.id,  Patient.is_active == True).all()
    
    return patients