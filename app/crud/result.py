from collections      import Counter

from fastapi.encoders import jsonable_encoder
from sqlmodel         import select

from app.crud.base    import CRUDBase
from app.models       import Result
from app.schemas      import ResultCreate, ResultUpdate


class CRUDResult(CRUDBase[Result, ResultCreate, ResultUpdate]):
    def get(self, db, answers):
        try:
            personalities = {
                "IJNT": "INTJ",
                "INPT": "INTP",
                "EJNT": "ENTJ",
                "ENPT": "ENTP",
                "FIJN": "INFJ",
                "FINP": "INFP",
                "EFJN": "ENFJ",
                "EFNP": "ENFP",
                "IJST": "ISTJ",
                "FIJS": "ISFJ",
                "EJST": "ESTJ",
                "EFJS": "ESFJ",
                "IPST": "ISTP",
                "FIPS": "ISFP",
                "EPST": "ESTP",
                "EFPS": "ESFP"
            }

            answer_lis  = [ answer for answer in answers ]
            personality = [
                value[0] for value in Counter(answer_lis).most_common(4)
            ]
            mbti        =  personalities[ ''.join(sorted(personality)) ]
            

            statement = select(self.model).where(
                self.model.personality == mbti
            )
            instance  = db.exec(statement).one()
            result    = jsonable_encoder(instance)

            return result


        finally:
            db.close()


result = CRUDResult(Result)