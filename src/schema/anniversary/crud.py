from pydantic import BaseModel


class AnniversaryBase(BaseModel):
    name: dict[str, str] | None
    image: str | None


class CreateAnniversary(AnniversaryBase):
    name: dict[str, str]
    image: str

    class Config:
        schema_extra = {
            "example": {
                "name": {"korean": "우정", "english": "Solid\nFriendship"},
                "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Friendship.svg",  # noqa: E501
            }
        }


class UpdateAnniversary(AnniversaryBase):
    class Config:
        schema_extra = {
            "example": {"name": {"korea": "사랑", "english": "Eternal\nLove"}}
        }
