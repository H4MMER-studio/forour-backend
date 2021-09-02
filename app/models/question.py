from sqlmodel import SQLModel, Field


class Question(SQLModel, table=True):
    __tablename__ = "questions"
    id: int = Field(primary_key=True)
    content: str