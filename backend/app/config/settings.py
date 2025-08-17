from pydantic_settings import BaseSettings
from pydantic import AnyUrl

class Settings(BaseSettings):
    APP_URL: AnyUrl
    VERIFICATION_TOKEN_TTL_HOURS: int = 24

    # DB Settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # For Email Settings
    """EMAIL_FROM: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str"""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
