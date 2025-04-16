from pydantic import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    GOOGLE_SHEETS_CREDENTIALS: str
    GOOGLE_SHEET_ID: str
    WEBHOOK_URL: str
    WEBHOOK_PATH: str = "/webhook"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
