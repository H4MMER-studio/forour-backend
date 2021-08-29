from pydantic import BaseSettings


class ProjectSettings(BaseSettings):
    TITLE: str = "ForOur"
    COMMON_API: str = "/api"


class LocalDatabaseSettings(BaseSettings):
    TYPE: str     = "postgresql"
    USER: str     = "forour"
    PASSWORD: str = "ForOur!@34"
    HOST: str     = "localhost"
    PORT: int     = 5432
    DB: str       = "forour"


project_settings        = ProjectSettings()
local_database_settings = LocalDatabaseSettings()