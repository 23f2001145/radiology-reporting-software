from pydantic import BaseModel
import enum

class ReportStatus(enum.Enum):
    draft = "draft"
    finalized = "finalized"

class CreateReport(BaseModel):
    patient_id: int
    template: int
    status: ReportStatus
