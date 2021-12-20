from typing import TypeVar, Generic, Optional, List
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from bson.objectid import ObjectId, InvalidId
from pymongo import ASCENDING, DESCENDING

CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)


class CRUDBase(Generic[CreateSchema, UpdateSchema]):
    def __init__(self, collection: str) -> None:
        self.collection = collection
    
    
    async def get_by_id(self, request: Request, id: str) -> Optional[dict]:
        try:
            document = await request.app.db[self.collection].find_one(
                {'_id': ObjectId(id)}
            )
            document['_id'] = str(document['_id'])
            
            return document
        
        except InvalidId:
            raise TypeError
    
    
    async def get_multi(
        self,
        request: Request,
        skip: int,
        limit: str,
        sort: Optional[List[str]]
    ) -> Optional[List[dict]]:
        query = request.app.db[self.collection]
        
        if sort:
            sort_field = []
            
            if not type(sort) is list:
                sort = list(type)
                
            for query_string in sort:
                field, option = query_string.split('')
            
                field = field.replace('-', '_')
                
                if option == 'asc':
                    option = ASCENDING
                elif option == 'desc':
                    option = DESCENDING
                else:
                    raise ValueError
                
                sort_field.append((field, option))
                
            query = query.sort(sort_field)
        
        documents = await query.skip(skip).limit(limit).to_list(length=None)
        
        for document in documents:
            document['_id'] = str(document['_id'])
        
        return documents
    
    
    async def create(
        self,
        request: Request,
        input_data: CreateSchema
    ) -> bool:
        inserted_document = await request.app.db[self.collection].insert_one(
            jsonable_encoder(input_data)
        )
        
        result = inserted_document.acknowledged
        
        return result
    
    
    async def update(
        self,
        request: Request,
        id: str,
        update_data: UpdateSchema
    ) -> bool:
        try:
            update_data = update_data.dict(exclude_none=True)
            
            updated_document = await request.app.db[
                self.collection
            ].find_one_and_update(
                {'_id': ObjectId(id)},
                {'$set': jsonable_encoder(update_data)},
                upsert=False
            )
            
            return updated_document
            
        except InvalidId:
            raise TypeError
    
    
    async def delete(self, request: Request, id: str) -> bool:
        try:
            deleted_document = await request.app.db[
                self.collection
            ].find_one_and_delete({
                '_id': ObjectId(id)
            })
            
            return deleted_document
        
        except InvalidId:
            raise TypeError