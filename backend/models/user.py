from sqlalchemy import String, Integer, DateTime, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    creation_time: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    reports: Mapped[List["Report"]] = relationship(
        back_populates="user", 
    )

    patients: Mapped[List["Patient"]] = relationship(
        back_populates="user"
    )