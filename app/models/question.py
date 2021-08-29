from sqlmodel import SQLModel, Field


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, auto_increment=True)
    content: str