from sqlalchemy import String, Integer, DateTime, func, ForeignKey, Date, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date
from db.base import Base
import enum

class Gender(enum.Enum):
    M = 'M'
    F = 'F'

class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    patient_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    dob: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[Gender] = mapped_column(SQLEnum(Gender), nullable=False)
    creation_time: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="patients"
    )

    reports: Mapped[List["Report"]] = relationship(
        back_populates="patient"
    )