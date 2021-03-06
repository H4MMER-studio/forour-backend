from pydantic import BaseModel


class ResultBase(BaseModel):
    flower_name: str | None
    flower_description: str | None
    images: dict[str, str] | None
    mbti: str | None
    mbti_title: str | None
    mbti_description: str | None
    mbti_relation: list[dict[str, str]] | None
    mbti_count: int | None = 0


class CreateResult(ResultBase):
    flower_name: str
    flower_description: str
    images: dict[str, str]
    mbti: str
    mbti_title: str
    mbti_description: str
    mbti_relation: list[dict[str, str]]
    mbti_count: int = 0

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
