from fastapi.encoders import jsonable_encoder
from sqlmodel         import select

from app.crud.base    import CRUDBase
from app.models       import Question
from app.schemas      import QuestionCreate, QuestionUpdate


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    pass


question = CRUDQuestion(Question)