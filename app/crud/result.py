from fastapi.encoders import jsonable_encoder
from sqlmodel         import select

from app.crud.base    import CRUDBase
from app.models       import Result
from app.schemas      import ResultCreate, ResultUpdate


class CRUDResult(CRUDBase[Result, ResultCreate, ResultUpdate]):
    def get(self, db, mbti):
        try:
            statement = select(self.model).where(
                self.model.personality == mbti
            )
            instance  = db.exec(statement).one()
            result    = jsonable_encoder(instance)

            return result


        finally:
            db.close()

result = CRUDResult(Result)