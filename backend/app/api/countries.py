"""Countries endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Country
from app.schemas.country import CountryResponse, CountryListResponse

router = APIRouter(prefix="/api/v1", tags=["countries"])


@router.get("/countries", response_model=CountryListResponse)
def get_countries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    countries = db.query(Country).offset(skip).limit(limit).all()
    total = db.query(Country).count()
    return CountryListResponse(
        total=total,
        countries=[CountryResponse.model_validate(c) for c in countries]
    )


@router.get("/countries/{country_id}", response_model=CountryResponse)
def get_country(country_id: int, db: Session = Depends(get_db)):
    country = db.query(Country).filter(Country.id == country_id).first()
    if not country:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Country not found"
        )
    return CountryResponse.model_validate(country)