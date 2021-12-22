from functools import lru_cache
from typing import List, Tuple

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LEVEL: str
    PROJECT_TITLE: str = "ForOur API 문서"
    PROJECT_VERSION: int = 2
    PROJECT_DESCRIPTION: str = "MBTI 검사를 통한 상대방에 어울리는 꽃 추천 서비스, ForOur API 문서"
    COMMON_API: str = "/api"
    DB_NAME: str
    MBTI_PAIR: List[Tuple[str, str]] = [
        ("E", "I"),
        ("N", "S"),
        ("F", "T"),
        ("P", "J"),
    ]

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
