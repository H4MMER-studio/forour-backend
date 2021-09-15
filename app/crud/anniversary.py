from fastapi.encoders import jsonable_encoder
from sqlmodel         import select

from app.crud.base    import CRUDBase
from app.models       import Anniversary
from app.schemas      import AnniversaryCreate, AnniversaryUpdate


class CRUDAnniversary(CRUDBase[Anniversary, AnniversaryCreate, AnniversaryUpdate]):
    def get(self, db, anniversary):
        try:
            statement = select(self.model).where(
                self.model.name == anniversary
            )

            instance = db.execute(statement).one()
            result   = jsonable_encoder(instance)

            return result

        finally:
            db.close()


anniversary = CRUDAnniversary(Anniversary)