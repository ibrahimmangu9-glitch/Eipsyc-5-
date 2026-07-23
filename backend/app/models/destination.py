"""Destination model"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models import Base


class Destination(Base):
    __tablename__ = "destinations"
    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    latitude = Column(Numeric(10, 8))
    longitude = Column(Numeric(11, 8))
    type = Column(String(50))
    best_season = Column(String(100))
    image_url = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    country = relationship("Country")

    def __repr__(self) -> str:
        return f"<Destination(id={self.id}, name={self.name})>"