from pydantic import BaseModel
from schemas.report_section import ReportSectionCreate, ReportSectionResponse
from models.report import ReportStatus
from datetime import datetime

class ReportCreate(BaseModel):
    patient_id: int
    template_id: int
    status: ReportStatus
    sections: list[ReportSectionCreate]

class ReportListResponse(BaseModel):
    id: int
    patient_name: str
    status: ReportStatus
    creation_time: datetime


class ReportResponse(BaseModel):
    id: int
    patient_id: int
    patient_name: str
    status: ReportStatus
    sections: list[ReportSectionResponse]
    

class ReportUpdate(BaseModel):
    status: ReportStatus
    sections: list[ReportSectionCreate]