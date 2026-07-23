"""Attraction model"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models import Base


class Attraction(Base):
    __tablename__ = "attractions"
    id = Column(Integer, primary_key=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"), nullable=False, index=True)
    name = Column(String(200), nullable=False)
    type = Column(String(50))
    description = Column(Text)
    latitude = Column(Numeric(10, 8))
    longitude = Column(Numeric(11, 8))
    entry_fee = Column(Numeric(10, 2))
    currency = Column(String(3), default="USD")
    image_url = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    destination = relationship("Destination")

    def __repr__(self) -> str:
        return f"<Attraction(id={self.id}, name={self.name})>"