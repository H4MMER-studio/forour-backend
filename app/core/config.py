import os

from pydantic import BaseSettings


class ProjectSettings(BaseSettings):
    TITLE: str = "ForOur"
    COMMON_API: str = "/api"


class DatabaseSettings(BaseSettings):
    USER     = os.getenv("POSTGRES_USER", "forour")
    PASSWORD = os.getenv("POSTGRES_PASSWORD", "ForOur!234")
    SERVER   = os.getenv("POSTGRES_SERVER", "forour.cqba6h2mznen.ap-northeast-2.rds.amazonaws.com")
    DB       = os.getenv("POSTGRES_DB", "forour")
    URL      = f"postgresql://{USER}:{PASSWORD}@{SERVER}/{DB}"


project_settings  = ProjectSettings()
database_settings = DatabaseSettings()