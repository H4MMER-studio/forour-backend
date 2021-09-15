from app.schemas.response import SuccessResponseBase


class GetAnniversaries(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": [
                    {
                        "english_name": "Solid\nFriendship",
                        "id": 1,
                        "name": "우정",
                        "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Friendship.svg"
                    },
                    {
                        "english_name": "Eternal\nLove",
                        "id": 2,
                        "name": "사랑",
                        "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Love.svg"
                    },
                    {
                        "english_name": "50th\nAnniversary",
                        "id": 3,
                        "name": "50일",
                        "image": "https://forour.s3.ap-northeast-2.amazonaws.com/50th.svg"
                    }
                ]
            }
        }


class GetAnniversary(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "Anniversary": {
                        "english_name": "Solid\nFriendship",
                        "id": 1,
                        "name": "우정",
                        "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Friendship.svg"
                    }
                }
            }
        }