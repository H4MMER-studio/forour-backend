import os

from pydantic import BaseSettings


class ProjectSettings(BaseSettings):
    TITLE: str = "ForOur"
    COMMON_API: str = "/api"


class LocalDatabaseSettings(BaseSettings):
    USER     = os.getenv("POSTGRES_USER", "forour")
    PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
    SERVER   = os.getenv("POSTGRES_SERVER", "localhost")
    DB       = os.getenv("POSTGRES_DB", "forour")
    URL      = f"postgresql://{USER}:{PASSWORD}@{SERVER}/{DB}"


project_settings        = ProjectSettings()
local_database_settings = LocalDatabaseSettings()