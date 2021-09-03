from fastapi.encoders import jsonable_encoder
from sqlmodel         import select

from app.crud.base    import CRUDBase
from app.models       import Question, Answer
from app.schemas      import QuestionCreate, QuestionUpdate


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    def get(self, db, id):
        try:
            statement = select(self.model, Answer).where(
                self.model.id == Answer.question_id
            ).where(self.model.id == id)
            instance  = db.exec(statement).one()
            result    = jsonable_encoder(instance)

            return result
        
        finally:
            db.close()


    def get_all(self, db):
        try:
            statement = select(self.model, Answer).where(
                self.model.id == Answer.question_id
            )
            instance  = db.exec(statement).all()
            result    = jsonable_encoder(instance)

            return result

        finally:
            db.close()


question = CRUDQuestion(Question)