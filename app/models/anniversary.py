import enum

from typing   import Optional

from sqlmodel import SQLModel, Field, Enum, Column


class AnniversaryType(str, enum.Enum):
    FRIENDSHIP     = "우정"
    LOVE            = "사랑"
    FIFTY           = "50일"
    ONE_HUNDREAD    = "100일"
    TWO_HUNDREAD    = "200일"
    THREE_HUNDREAD  = "300일"
    ONE_THOUSAND    = "1000일"
    FIRST_YAER      = "1주년"
    SECOND_YEAR     = "2주년"
    THIRD_YEAR      = "3주년"
    NTH_YEAR        = "n주년"
    MARRIAGE        = "결혼"
    DELIVERY        = "출산"
    VALENTINE_DAY   = "발렌타인데이"
    WHITE_DAY       = "화이트데이"
    CHRISTMAS       = "크리스마스"
    NEW_YAER        = "새해"
    PASS_THE_TEST   = "합격"
    HOMECOMING      = "귀국"
    GRADUATION      = "졸업"
    SCHOOL_ENTRANCE = "입학"
    BIRTHDAY        = "생일"
    EMPLOYMENT      = "취업"
    CONCERT         = "공연"
    EXHIBITION      = "전시"


class Anniversary(SQLModel, table=True):
    __tablename__ = "anniversaries"

    id: Optional[int] = Field(default=None, primary_key=True)