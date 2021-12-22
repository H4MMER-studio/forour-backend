from typing import Optional

from fastapi import Request
from pymongo import ReturnDocument

from src.crud.base import CRUDBase
from src.schema import CreateResult, UpdateResult
from src.util import answers_parser


class CRUDResult(CRUDBase[CreateResult, UpdateResult]):
    async def get_one(self, request: Request, answers: str) -> Optional[dict]:
        answer = answers_parser(answers=answers)
        document = await request.app.db[self.collection].find_one_and_update(
            {"mbti": answer},
            {"$inc": {"mbti_count": 1}},
            return_document=ReturnDocument.AFTER,
        )

        document["_id"] = str(document["_id"])

        return document


result_crud = CRUDResult(collection="results")
