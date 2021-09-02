from sqlmodel import SQLModel, Field


class Answer(SQLModel, table=True):
    __tablename__ = "answers"
    id: int = Field(primary_key=True)
    content_a: dict
    content_b: dict
    question_id: int = Field(foreign_key="questions.id")