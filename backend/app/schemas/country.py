"""Country schemas"""

from pydantic import BaseModel
from typing import List, Optional


class CountryResponse(BaseModel):
    id: int
    name: str
    code: str
    capital: Optional[str]
    region: Optional[str]
    currency: Optional[str]
    language: Optional[str]
    flag_url: Optional[str]
    description: Optional[str]

    class Config:
        from_attributes = True


class CountryListResponse(BaseModel):
    total: int
    countries: List[CountryResponse]