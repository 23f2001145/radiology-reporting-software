from pydantic import BaseModel
from models.report_section import SectionType

class UpdateSection(BaseModel):
    section_type: SectionType
    content: str

class ReportSectionCreate(BaseModel):
    section_type: SectionType
    content: str

class ReportSectionResponse(BaseModel):
    section_type: SectionType
    content: str