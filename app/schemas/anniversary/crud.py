from typing import Optional
from sqlmodel   import SQLModel

from app.models import AnniversaryType


class AnniversaryBase(SQLModel):
    name: AnniversaryType
    english_name: str
    image: str


class AnniversaryCreate(AnniversaryBase):
    
    class Config:
        schema_extra = {
            "example": {

            }
        }


class AnniversaryUpdate(AnniversaryBase):
    id: int

    class Config:
        schema_extra = {
            "example": {

            }
        }