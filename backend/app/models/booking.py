"""Booking model"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum

from app.models import Base


class BookingStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    accommodation_id = Column(Integer, ForeignKey("accommodations.id"), nullable=False, index=True)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    number_of_guests = Column(Integer, nullable=False)
    total_price = Column(Numeric(10, 2))
    currency = Column(String(3), default="USD")
    status = Column(Enum(BookingStatus), default=BookingStatus.PENDING, nullable=False, index=True)
    special_requests = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    user = relationship("User")
    accommodation = relationship("Accommodation")

    def __repr__(self) -> str:
        return f"<Booking(id={self.id}, status={self.status})>"