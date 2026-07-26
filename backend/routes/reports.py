from fastapi import APIRouter, HTTPException, status, File, UploadFile, Depends
from sqlalchemy.orm import Session
from typing import List

from services.pipeline_service import generate_report
from core.deps import get_db
from auth.dependencies import get_current_active_user
from models.user import User
from models.report import Report, ReportStatus
from models.patient import Patient
from models.report_section import ReportSection
from schemas.report import ReportCreate, ReportListResponse, ReportResponse, ReportUpdate
from schemas.report_section import ReportSectionResponse

router = APIRouter(prefix="/reports", tags=["reports"])

@router.post("/transcribe", status_code=status.HTTP_200_OK)
def transcribe_report(audio_file: UploadFile = File(...)) -> dict:
    try:
        print(audio_file.filename)
        print(audio_file.content_type)
        print(type(audio_file.file))
        print(audio_file.file.name)

        report = generate_report(audio_file.filename, audio_file.file)

        return report
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/save", status_code=status.HTTP_201_CREATED)
def save_report(report: ReportCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    try:
        # 1 is the placeholder templated id 
        new_report = Report(
            patient_id=report.patient_id,
            user_id=current_user.id,
            template_id=1,
            status=report.status
        )

        db.add(new_report)
        db.flush()  
        for section in report.sections:
            db.add(
                ReportSection(
                    report_id=new_report.id,
                    section_type=section.section_type,
                    content=section.content
                )
            )

        db.commit()
        db.refresh(new_report)

        return {
            "message": "Report saved successfully",
            "report_id": new_report.id
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("", response_model=List[ReportListResponse])
def get_reports(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    reports = (
        db.query(Report)
        .join(Patient)
        .filter(Report.user_id == current_user.id)
        .order_by(Report.creation_time.desc())
        .all()
    )

    return [
        ReportListResponse(
            id=report.id,
            patient_name=report.patient.patient_name,
            status=report.status,
            creation_time=report.creation_time,
        )
        for report in reports
    ]


@router.get("/{report_id}", response_model=ReportResponse)
def get_report(report_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    report = (
        db.query(Report)
        .filter(
            Report.id == report_id,
            Report.user_id == current_user.id
        )
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )

    return ReportResponse(
        id=report.id,
        patient_id=report.patient_id,
        patient_name=report.patient.patient_name,
        status=report.status,
        sections=[
            ReportSectionResponse(
                section_type=section.section_type,
                content=section.content
            )
            for section in report.sections
        ]
    )


@router.put("/{report_id}", status_code=status.HTTP_200_OK)
def update_report(
    report_id: int,
    report: ReportUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    try:

        existing_report = (
            db.query(Report)
            .filter(
                Report.id == report_id,
                Report.user_id == current_user.id,
            )
            .first()
        )

        if existing_report is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Report not found",
            )

        if existing_report.status == ReportStatus.finalized:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Finalized reports cannot be edited.",
            )

        existing_report.status = report.status

        for updated_section in report.sections:
            section = (
                db.query(ReportSection)
                .filter(
                    ReportSection.report_id == report_id,
                    ReportSection.section_type == updated_section.section_type,
                )
                .first()
            )

            if section is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Section '{updated_section.section_type}' not found",
                )

            section.content = updated_section.content

        db.commit()
        db.refresh(existing_report)

        return {
            "message": "Report updated successfully"
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
