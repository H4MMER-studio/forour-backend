from typing   import Optional
from sqlmodel import SQLModel, Field


class Question(SQLModel, table=True):
    __tablename__ = "questions"
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str