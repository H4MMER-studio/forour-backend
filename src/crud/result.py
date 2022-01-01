from typing import List, Optional

from fastapi import Request
from pymongo import ASCENDING, DESCENDING, ReturnDocument

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

    async def get_multi(
        self,
        request: Request,
        skip: int,
        limit: str,
        sort: Optional[List[str]],
    ) -> Optional[List[dict]]:

        if sort:
            sort_field = []

            if not type(sort) is list:
                sort = list(type)

            for query_string in sort:
                field, option = query_string.split(" ")

                field = field.replace("-", "_")

                if option == "asc":
                    option = ASCENDING
                elif option == "desc":
                    option = DESCENDING
                else:
                    raise ValueError

                sort_field.append((field, option))

        documents = (
            await request.app.db[self.collection]
            .find()
            .skip(skip)
            .limit(limit)
            .to_list(length=None)
        )

        for document in documents:
            document["_id"] = str(document["_id"])

        return documents


result_crud = CRUDResult(collection="results")
