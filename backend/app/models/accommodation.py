"""Accommodation model"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models import Base


class Accommodation(Base):
    __tablename__ = "accommodations"
    id = Column(Integer, primary_key=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"), nullable=False, index=True)
    operator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    name = Column(String(200), nullable=False)
    type = Column(String(50))
    description = Column(Text)
    price_per_night = Column(Numeric(10, 2))
    currency = Column(String(3), default="USD")
    rooms_available = Column(Integer)
    latitude = Column(Numeric(10, 8))
    longitude = Column(Numeric(11, 8))
    rating = Column(Numeric(3, 2))
    image_url = Column(String(500))
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    destination = relationship("Destination")
    operator = relationship("User")

    def __repr__(self) -> str:
        return f"<Accommodation(id={self.id}, name={self.name})>"