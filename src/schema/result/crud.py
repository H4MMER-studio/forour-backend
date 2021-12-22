from typing import Dict, Optional

from pydantic import BaseModel


class ResultBase(BaseModel):
    flower_name: str
    flower_description: str
    images: Dict[str, str]
    mbti: str
    mbti_title: str
    mbti_description: str
    mbti_relation: Dict[str, str]


class CreateResult(ResultBase):
    mbti_count: int = 0

    class Config:
        schema_extra = {"example": {}}


class UpdateResult(ResultBase):
    flower_name: Optional[str]
    flower_description: Optional[str]
    images: Optional[Dict[str, str]]
    mbti: Optional[str]
    mbti_title: Optional[str]
    mbti_description: Optional[str]

    class Config:
        schema_extra = {"example": {}}
