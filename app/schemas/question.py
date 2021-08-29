from sqlmodel import SQLModel


class QuestionBase(SQLModel):
    id: int
    content: str


class QuestionRead(QuestionBase):

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "content": "1. 처음에 둘은 어떻게 친해졌나요?"
            }
        }