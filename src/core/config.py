from functools import lru_cache
from typing import List, Tuple

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LEVEL: str
    DB_NAME: str = "forour"
    HOST: str = "0.0.0.0"
    PROJECT_TITLE: str = "ForOur API 문서"
    PROJECT_VERSION: int = 2
    PROJECT_DESCRIPTION: str = "MBTI 검사를 통한 상대방에 어울리는 꽃 추천 서비스, ForOur API 문서"
    COMMON_API: str = "/api"
    MBTI_PAIR: List[Tuple[str, str]] = [
        ("E", "I"),
        ("N", "S"),
        ("F", "T"),
        ("P", "J"),
    ]

    class Config:
        env_file = ".env"


class DevelopSettings(Settings):
    PORT: int = 8000
    RELOAD: bool = True
    DB_URL: str = Field(env="DEVELOP_DB_URL")


class ProductSettings(Settings):
    PORT: int = 80
    RELOAD: bool = False
    DB_URL: str = Field(env="PRODUCT_DB_URL")


@lru_cache
def get_settings():
    if Settings().LEVEL == "DEVELOP":
        return DevelopSettings()
    else:
        return ProductSettings()
