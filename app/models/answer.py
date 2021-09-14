from typing   import Optional, Dict

from sqlmodel import SQLModel, Field, Column, JSON


class Answer(SQLModel, table=True):
    __tablename__ = "answers"
    id: Optional[int] = Field(default=None, primary_key=True)
    content_a: Dict[str, str] = Field(
        sa_column=Column("content_a", JSON, nullable=False)
    )
    content_b: Dict[str, str] = Field(
        sa_column=Column("content_b", JSON, nullable=False)
    )
    question_id: int = Field(foreign_key="questions.id")