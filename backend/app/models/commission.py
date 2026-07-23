"""Commission model"""

from sqlalchemy import Column, String, DateTime, ForeignKey, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum

from app.models import Base


class CommissionStatus(str, enum.Enum):
    PENDING = "pending"
    CALCULATED = "calculated"
    SETTLED = "settled"
    PAID = "paid"


class Commission(Base):
    __tablename__ = "commissions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    payment_id = Column(UUID(as_uuid=True), ForeignKey("payments.id"), nullable=False, index=True)
    accommodation_id = Column(Integer, ForeignKey("accommodations.id"), nullable=False, index=True)
    provider_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    commission_rate = Column(Numeric(5, 2), nullable=False)
    commission_amount = Column(Numeric(10, 2), nullable=False)
    provider_payout = Column(Numeric(10, 2))
    status = Column(Enum(CommissionStatus), default=CommissionStatus.PENDING, nullable=False)
    settled_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    payment = relationship("Payment")
    accommodation = relationship("Accommodation")
    provider = relationship("User")

    def __repr__(self) -> str:
        return f"<Commission(id={self.id}, status={self.status})>"