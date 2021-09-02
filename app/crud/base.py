from typing           import Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic         import BaseModel
from sqlmodel         import select

from app.database     import Base


ModelType        = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model


    def get(self, db, id):
        try:
            instance = db.get(self.model, id)
            result   = jsonable_encoder(instance)

            return result
        
        finally:
            db.close()


    def get_multi(self, db, skip, limit):
        try:
            instance = db.exec(select(self.model).offset(skip).limit(limit)).all()
            result   = jsonable_encoder(instance)

            return result

        finally:
            db.close()


    def create(self, db, obj_in: CreateSchemaType):
        try:
            instance = self.model.from_orm(obj_in)
            db.add(instance)
            db.commit()
            db.refresh(instance)

            result = jsonable_encoder(instance)

            return result
        
        finally:
            db.close()


    def update(self, db, id, obj_in: UpdateSchemaType):
        try:
            instance = db.get(self.model, id)
            if not instance:
                pass

            obj_data = obj_in.dict(exclude=True)

            for key, value in obj_data.items():
                setattr(instance, key, value)

            db.add(instance)
            db.commit()
            db.refresh(instance)

            result = jsonable_encoder(instance)

            return result

        finally:
            db.close()


    def remove(self, db, id):
        try:
            instance = db.get(self.model, id)
            if not instance:
                pass
            
            db.delete(instance)
            db.commit()
            db.refresh(instance)

            result = jsonable_encoder(instance)

            return result

        finally:
            db.close()