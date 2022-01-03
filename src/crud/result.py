from typing import List, Optional

from fastapi import Request
from pymongo import ASCENDING, DESCENDING

from src.crud.base import CRUDBase
from src.schema import CreateResult, UpdateResult
from src.util import answers_parser


class CRUDResult(CRUDBase[CreateResult, UpdateResult]):
    async def get_one(self, request: Request, answers: str) -> Optional[dict]:
        answer = answers_parser(answers=answers)

        await request.app.db[self.collection].update_one(
            {"mbti": answer}, {"$inc": {"mbti_count": 1}}
        )

        document = (
            await request.app.db[self.collection]
            .aggregate(
                [
                    {"$match": {"mbti": answer}},
                    {"$unwind": "$mbti_relation"},
                    {
                        "$lookup": {
                            "from": "results",
                            "localField": "mbti_relation.mbti",
                            "foreignField": "mbti",
                            "as": "mbti_relation.information",
                        }
                    },
                    {
                        "$addFields": {
                            "mbti_relation._id": {
                                "$first": "$mbti_relation.information._id"
                            },
                            "mbti_relation.mbti_description": {
                                "$first": "$mbti_relation.information.mbti_description"  # noqa E501
                            },
                            "mbti_relation.mbti_title": {
                                "$first": "$mbti_relation.information.mbti_title"  # noqa E501
                            },
                            "mbti_relation.mbti_count": {
                                "$first": "$mbti_relation.information.mbti_count"  # noqa E501
                            },
                            "mbti_relation.images": {
                                "$first": "$mbti_relation.information.images"
                            },
                            "mbti_relation.flower_name": {
                                "$first": "$mbti_relation.information.flower_name"  # noqa #501
                            },
                            "mbti_relation.flower_description": {
                                "$first": "$mbti_relation.information.flower_description"  # noqa E501
                            },
                        }
                    },
                    {
                        "$group": {
                            "_id": "$_id",
                            "images": {"$first": "$images"},
                            "mbti": {"$first": "$mbti"},
                            "mbti_title": {"$first": "$mbti_title"},
                            "mbti_count": {"$first": "$mbti_count"},
                            "mbti_description": {
                                "$first": "$mbti_description"
                            },
                            "flower_name": {"$first": "$flower_name"},
                            "flower_description": {
                                "$first": "$flower_description"
                            },
                            "mbti_relation": {"$push": "$mbti_relation"},
                        }
                    },
                    {"$unset": "mbti_relation.information"},
                ]
            )
            .to_list(length=1)
        )

        for mbti_relation in document[0]["mbti_relation"]:
            mbti_relation["_id"] = str(mbti_relation["_id"])

        document[0]["_id"] = str(document[0]["_id"])

        return document[0]

    async def get_multi(
        self,
        request: Request,
        skip: int,
        limit: int,
        sort: Optional[List[str]],
    ) -> Optional[List[dict]]:

        query = [
            {"$unwind": "$mbti_relation"},
            {
                "$lookup": {
                    "from": "results",
                    "localField": "mbti_relation.mbti",
                    "foreignField": "mbti",
                    "as": "mbti_relation.information",
                }
            },
            {
                "$addFields": {
                    "mbti_relation._id": {
                        "$first": "$mbti_relation.information._id"
                    },
                    "mbti_relation.mbti_description": {
                        "$first": "$mbti_relation.information.mbti_description"  # noqa E501
                    },
                    "mbti_relation.mbti_title": {
                        "$first": "$mbti_relation.information.mbti_title"
                    },
                    "mbti_relation.mbti_count": {
                        "$first": "$mbti_relation.information.mbti_count"
                    },
                    "mbti_relation.images": {
                        "$first": "$mbti_relation.information.images"
                    },
                    "mbti_relation.flower_name": {
                        "$first": "$mbti_relation.information.flower_name"
                    },
                    "mbti_relation.flower_description": {
                        "$first": "$mbti_relation.information.flower_description"  # noqa E501
                    },
                }
            },
            {
                "$group": {
                    "_id": "$_id",
                    "images": {"$first": "$images"},
                    "mbti": {"$first": "$mbti"},
                    "mbti_title": {"$first": "$mbti_title"},
                    "mbti_count": {"$first": "$mbti_count"},
                    "mbti_description": {"$first": "$mbti_description"},
                    "flower_name": {"$first": "$flower_name"},
                    "flower_description": {"$first": "$flower_description"},
                    "mbti_relation": {"$push": "$mbti_relation"},
                }
            },
            {"$unset": "mbti_relation.information"},
        ]

        if sort:
            sort_field = {}

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

                sort_field[field] = option

            query.append({"$sort": sort_field})

        if skip:
            query.append({"$skip": skip})

        if limit:
            query.append({"$limit": limit})

        documents = (
            await request.app.db[self.collection]
            .aggregate(query)
            .to_list(length=None)
        )

        for document in documents:
            document["_id"] = str(document["_id"])

            for mbti_relation in document["mbti_relation"]:
                mbti_relation["_id"] = str(document["_id"])

        return documents


result_crud = CRUDResult(collection="results")
