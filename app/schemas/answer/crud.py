from sqlmodel import SQLModel


class AnswerBase(SQLModel):
    content_a: dict
    content_b: dict


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