from fastapi.encoders import jsonable_encoder
from sqlmodel         import select

from app.crud.base    import CRUDBase
from app.models       import Question
from app.schemas      import QuestionCreate, QuestionUpdate



class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    def get_all(self, db):
        instance = db.exec(select(self.model)).all()
        result   = jsonable_encoder(instance)

        db.close()
        
        return result


question = CRUDQuestion(Question)