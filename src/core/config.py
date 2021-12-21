from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LEVEL: str
    PROJECT_TITLE: str = "꽃 추천 서비스, ForOur"
    COMMON_API: str = "/api"
    DB_NAME: str

    class Config:
        env_file = ".env"


class DevelopSettings(Settings):
    DB_URL: str = Field("DEVELOP_DB_URL")


class ProductSettings(Settings):
    DB_URL: str = Field("PRODUCT_DB_URL")


@lru_cache
def get_settings():
    if Settings().LEVEL == "DEVELOP":
        return DevelopSettings()
    else:
        return ProductSettings()
