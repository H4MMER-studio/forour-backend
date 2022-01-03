from typing import Dict, List, Optional

from pydantic import BaseModel


class ResultBase(BaseModel):
    flower_name: str
    flower_description: str
    images: Dict[str, str]
    mbti: str
    mbti_title: str
    mbti_description: str
    mbti_relation: List[Dict[str, str]]
    mbti_count: int = 0


class CreateResult(ResultBase):
    class Config:
        schema_extra = {
            "example": {
                "flower_name": "프리지아",
                "flower_description": "순진과 천진난만",
                "images": {
                    "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ENFJ_%E1%84%91%E1%85%B3%E1%84%85%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%8B%E1%85%A1.svg",  # noqa: E501
                    "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ENFJ.png",  # noqa: E501
                },
                "mbti": "ENFJ",
                "mbti_count": 0,
                "mbti_title": "정의로운 사회운동가",
                "mbti_description": "넘치는 카리스마와 영향력으로 청중을 압도하는 리더형",
                "mbti_relation": {"good": "ISTP", "bad": "ISTJ"},
            }
        }


class UpdateResult(ResultBase):
    flower_name: Optional[str]
    flower_description: Optional[str]
    images: Optional[Dict[str, str]]
    mbti: Optional[str]
    mbti_title: Optional[str]
    mbti_description: Optional[str]
    mbti_relation: Optional[List[Dict[str, str]]]
    mbti_count: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "flower_description": "팔방미인 또는 고집쟁이",
                "images": {
                    "result": "https://forour.s3.ap-northeast-2.amazonaws.com/ENFP_%E1%84%85%E1%85%B5%E1%84%8B%E1%85%A1%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%E1%84%89%E1%85%B3.svg",  # noqa: E501
                    "kakao": "https://forour.s3.ap-northeast-2.amazonaws.com/ENFP.png",  # noqa: E501
                },
            }
        }
