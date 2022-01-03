from src.schema.response import ErrorResponseModel, GetResponseModel

anniversary_get_multi_response = {
    "200": {
        "model": GetResponseModel,
        "description": "성공",
        "content": {"application/json": {"example": {"data": [
            {
                "_id": "61c9d790bae9d99ea4c1782c",
                "name": {
                    "korean": "우정",
                    "english": "Solid\nFriendship"
                },
                "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Friendship.svg"
            },
            {
                "_id": "61c9d79dbae9d99ea4c1782d",
                "name": {
                    "korean": "사랑",
                    "english": "Eternal\nLove"
                },
                "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Love.svg"
            }]}}},
    },
    "404": {
        "model": GetResponseModel,
        "description": "존재하지 않는 엔티티",
        "content": {"application/json": {"example": {"data": []}}},
    },
    "422": {
        "model": ErrorResponseModel,
        "description": "유효하지 않은 매개변수 사용",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["query", "skip"],
                            "msg": "field required",
                            "type": "value_error.missing",
                        }
                    ]
                }
            }
        },
    },
}
