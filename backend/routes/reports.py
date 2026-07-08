from fastapi import APIRouter, HTTPException, status, File, UploadFile
from services.pipeline_service import generate_report

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