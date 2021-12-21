from src.schema.response import ErrorResponseModel, GetResponseModel

question_get_by_id_response = {
    "200": {
        "model": GetResponseModel,
        "description": "성공",
        "content": {
            "application/json": {
                "example": {
                    "data": {
                        "_id": "61b9a8290a71a767f5684471",
                        "question_order": 1,
                        "question": "처음에 둘은 어떻게 친해졌나요?",
                        "answers": [
                            {
                                "id": 1,
                                "content": "name이(가) 먼저 제게 말을 걸어줬어요.",
                                "personality": "E",
                            },
                            {
                                "id": 2,
                                "content": "제가 name에게 먼저 말을 걸었어요.",
                                "personality": "I",
                            },
                        ],
                    }
                }
            }
        },
    },
    "400": {
        "model": ErrorResponseModel,
        "description": "유효하지 않은 ObjectId",
        "content": {
            "application/json": {
                "example": {"detail": "ObjectId 1234 Invalid"}
            }
        },
    },
    "404": {
        "model": GetResponseModel,
        "description": "존재하지 않는 엔티티",
        "content": {"application/json": {"example": {"data": []}}},
    },
}
