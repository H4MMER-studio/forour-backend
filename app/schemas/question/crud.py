from sqlmodel import SQLModel


class QuestionBase(SQLModel):
    content: str


class QuestionCreate(QuestionBase):
    
    class Config:
        schema_extra = {
            "example": {
                "content": "처음에 둘은 어떻게 친해졌나요?"
            }
        }


class QuestionUpdate(QuestionBase):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "content": "처음에 둘은 어떻게 친해졌나요?"
            }
        }


class QuestionRead(QuestionBase):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "content": "처음에 둘은 어떻게 친해졌나요?"
            }
        }