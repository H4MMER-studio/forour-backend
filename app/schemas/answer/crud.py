from typing   import Dict
from sqlmodel import SQLModel


class AnswerBase(SQLModel):
    content_a: Dict[str, str]
    content_b: Dict[str, str]


class AnswerCreate(AnswerBase):
    question_id: int


    class Config:
        schema_extra = {
            "example": {

            }
        }


class AnswerUpdate(AnswerBase):
    id: int

    class Config:
        schema_extra = {
            "example": {

            }
        }