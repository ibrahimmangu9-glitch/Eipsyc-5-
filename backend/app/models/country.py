"""Country model"""

from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.models import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    code = Column(String(3), unique=True, nullable=False)
    capital = Column(String(100))
    region = Column(String(100))
    currency = Column(String(10))
    language = Column(String(100))
    flag_url = Column(String(500))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<Country(id={self.id}, name={self.name}, code={self.code})>"