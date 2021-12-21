from typing import Dict, Optional

from pydantic import BaseModel


class AnniversaryBase(BaseModel):
    name: Dict[str, str]
    image: str


class CreateAnniversary(AnniversaryBase):
    class Config:
        schema_extra = {
            "example": {
                "name": {"korean": "우정", "english": "Solid\nFriendship"},
                "image": "https://forour.s3.ap-northeast-2.amazonaws.com/Friendship.svg",  # noqa: E501
            }
        }


class UpdateAnniversary(AnniversaryBase):
    name: Optional[Dict[str, str]]
    image: Optional[str]

    class Config:
        schema_extra = {
            "example": {"name": {"korea": "사랑", "english": "Eternal\nLove"}}
        }
