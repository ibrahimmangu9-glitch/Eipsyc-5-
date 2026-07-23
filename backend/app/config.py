"""Application configuration"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings from environment variables"""

    APP_NAME: str = "EIPSYC5 AFRICA"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    REDIS_URL: str = "redis://localhost:6379"
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:8000"
    GOOGLE_MAPS_API_KEY: Optional[str] = None
    STRIPE_SECRET_KEY: Optional[str] = None
    FLUTTERWAVE_SECRET_KEY: Optional[str] = None
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    COMMISSION_HOTEL_PERCENT: float = 10.0
    COMMISSION_OPERATOR_PERCENT: float = 15.0
    COMMISSION_ACCOMMODATION_PERCENT: float = 15.0
    COMMISSION_ACTIVITY_PERCENT: float = 5.0
    EIPSYC5_OWNER_PAYOUT_ACCOUNT: str = "PLACEHOLDER_SECURE_BACKEND_ONLY"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()