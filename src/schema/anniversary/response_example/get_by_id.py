from src.schema.response import ErrorResponseModel, GetResponseModel

anniversary_get_by_id_response = {
    "200": {
        "model": GetResponseModel,
        "description": "성공",
        "content": {"application/json": {"example": {"data":
            {
                "_id": "61c9d790bae9d99ea4c1782c",
                    "name": {
                        "korean": "우정",
                        "english": "Solid\nFriendship"
                    },
                    "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Friendship.svg"

            }
        }}},
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
