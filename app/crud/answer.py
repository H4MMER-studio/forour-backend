from app.crud.base import CRUDBase
from app.models    import Answer
from app.schemas   import AnswerCreate, AnswerUpdate


class CRUDAnswer(CRUDBase[Answer, AnswerCreate, AnswerUpdate]):
    pass

answer = CRUDAnswer(Answer)