import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    SERVER_HOST: str
    SERVER_PORT: int

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE)
    )

    def get_db_url(self) -> str:
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

    def get_server_connect(self) -> tuple[str, int]:
        return (self.SERVER_HOST, self.SERVER_PORT)

settings = Settings()