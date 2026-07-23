from fastapi import APIRouter, HTTPException, status, File, UploadFile, Depends
from sqlalchemy.orm import Session
from services.pipeline_service import generate_report
from core.deps import get_db
from auth.dependencies import get_current_active_user
from models.user import User
from models.report import Report
from models.report_section import ReportSection
from schemas.report import ReportCreate

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