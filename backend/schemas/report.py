from pydantic import BaseModel
from schemas.report_section import ReportSectionCreate
from models.report import ReportStatus

class ReportCreate(BaseModel):
    patient_id: int
    template_id: int
    status: ReportStatus
    sections: list[ReportSectionCreate]