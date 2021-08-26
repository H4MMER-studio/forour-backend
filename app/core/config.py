from pydantic import BaseSettings


class ProjectSettings(BaseSettings):
    TITLE: str = "ForOur"
    COMMON_API: str = "/api"

project_settings = ProjectSettings()