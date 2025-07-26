from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
from pydantic import Field
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()

ENV_MAP = {
    "development": BASE_DIR / "core/env/.env.development",
    "docker": BASE_DIR / "core/env/.env.docker",
    "homolog": BASE_DIR / "core/env/.env.homolog",
    "production": BASE_DIR / "core/env/.env.production"
}

load_dotenv(dotenv_path=str(ENV_MAP.get(ENVIRONMENT, BASE_DIR / "core/env/.env.development")))

class Settings(BaseSettings):
    APP_NAME: str = Field(..., alias="APP_NAME")
    ENVIRONMENT: str = Field(default=ENVIRONMENT, alias="ENVIRONMENT")
    DEBUG: bool = Field(default=True, alias="DEBUG")

    ORACLE_HOST: str = Field(default="localhost", alias="ORACLE_HOST")
    ORACLE_PORT: int = Field(default=1521, alias="ORACLE_PORT")
    ORACLE_SERVICE: str = Field(default="xe", alias="ORACLE_SERVICE")
    ORACLE_USER: str = Field(default="system", alias="ORACLE_USER")
    ORACLE_PASSWORD: str = Field(default="oracle", alias="ORACLE_PASSWORD")

    MONGO_LOG_CONN: str = Field(..., alias="MONGO_LOG_CONN")
    MONGO_LOG_DB: str = Field(..., alias="MONGO_LOG_DB")
    MONGO_LOG_COLLECTION: str = Field(..., alias="MONGO_LOG_COLLECTION")

    REDIS_HOST: str = Field(..., alias="REDIS_HOST")
    REDIS_PORT: int = Field(..., alias="REDIS_PORT")
    REDIS_DB: int = Field(..., alias="REDIS_DB")
    REDIS_PASSWORD: str = Field(..., alias="REDIS_PASSWORD")

    class Config:
        populate_by_name = True
        extra = "forbid"

@lru_cache()
def GetSettings():
    return Settings()