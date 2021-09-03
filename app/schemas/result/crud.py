from sqlmodel   import SQLModel

from app.models import Personality


class ResultBase(SQLModel):
    flower: str
    description: str
    image: str
    personality: Personality


class ResultCreate(ResultBase):

    class Config:
        schema_extra = {
            "example": {

            }
        }


class ResultUpdate(ResultBase):
    id: int

    class Config:
        schema_extra = {
            "example": {

            }
        }