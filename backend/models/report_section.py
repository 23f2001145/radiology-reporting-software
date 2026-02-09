from sqlalchemy import Integer, DateTime, String, func, ForeignKey, Enum as SQLEnum, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship
import enum

from db.base import Base

class SectionType(enum.Enum):
    findings = "findings"
    impression = "impression"
    advice = "advice"

class ReportSection(Base):
    __tablename__ = "report_sections"
    __table_args__ = (
        UniqueConstraint("report_id", "section_type", name="uq_report_section"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    section_type: Mapped[SectionType] = mapped_column(SQLEnum(SectionType), nullable= False)
    report_id: Mapped[int] = mapped_column(ForeignKey("reports.id"), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=True)
    creation_time: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_time: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    report: Mapped["Report"] = relationship(
        back_populates="sections"
    )