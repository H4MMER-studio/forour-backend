import enum

from typing   import Optional

from sqlmodel import SQLModel, Field, Enum, Column


class Personality(str, enum.Enum):
    INTJ = "INTJ"
    INTP = "INTP"
    ENTJ = "ENTJ"
    ENTP = "ENTP"
    INFJ = "INFJ"
    INFP = "INFP"
    ENFJ = "ENFJ"
    ENFP = "ENFP"
    ISTJ = "ISTJ"
    ISFJ = "ISFJ"
    ESTJ = "ESTJ"
    ESFJ = "ESFJ"
    ISTP = "ISTP"
    ISFP = "ISFP"
    ESTP = "ESTP"
    ESFP = "ESFP"


class Result(SQLModel, table=True):
    __tablename__ = "results"

    id: Optional[int] = Field(default=None, primary_key=True)
    flower: str
    description: str
    image: str
    personality: Personality = Field(
        sa_column=Column("personality", Enum(Personality), nullable=False)
    )
    to_whom: str
    anniversary_id: int = Field(foreign_key="anniversaries_id")