from sqlalchemy import Integer, String, DateTime, func, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from typing import List
from db.base import Base

class ReportStatus(enum.Enum):
    draft = "draft"
    finalized = "finalized"

class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), nullable=False)
    template_id: Mapped[int] = mapped_column(ForeignKey("templates.id"), nullable=False)
    status: Mapped[ReportStatus] = mapped_column(SQLEnum(ReportStatus), nullable=False, default=ReportStatus.draft, server_default=ReportStatus.draft.value)
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

    user: Mapped["User"] = relationship(
        back_populates="reports"
    )

    sections: Mapped[List["ReportSection"]] = relationship(
        back_populates="report",
        cascade="all, delete-orphan"
    )

    template: Mapped["Template"] = relationship(
        back_populates="reports"
    )

    patient: Mapped["Patient"] = relationship(
        back_populates="reports"
    )