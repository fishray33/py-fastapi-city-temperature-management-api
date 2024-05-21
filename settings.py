from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "City temperature management FastAPI"

    DATABASE_URL: str | None = "sqlite+aiosqlite:///./city-temperature.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
