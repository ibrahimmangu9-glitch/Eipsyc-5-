"""Operator model"""

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Numeric, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models import Base


class Operator(Base):
    __tablename__ = "operators"
    id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    company_name = Column(String(200), nullable=False)
    registration_number = Column(String(100), unique=True)
    description = Column(Text)
    website = Column(String(500))
    phone = Column(String(20))
    rating = Column(Numeric(3, 2))
    is_verified = Column(Boolean, default=False)
    specialties = Column(String(500))
    years_in_business = Column(Integer)
    employee_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    user = relationship("User", foreign_keys=[id])

    def __repr__(self) -> str:
        return f"<Operator(id={self.id}, company_name={self.company_name})>"