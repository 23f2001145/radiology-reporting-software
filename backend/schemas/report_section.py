from pydantic import BaseModel
from enum import Enum

class SectionType(Enum):
    findings = "findings"
    impression = "impression"
    advice = "advice"

class UpdateSection:
    section_type: str
    content: str