from app.schemas.response import SuccessResponseBase


class GetResultResponse(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "flower_description": "자존감",
                    "id": 11,
                    "mbti_description": "상상력이 풍부하며 철추철미한 계획을 세우는 전략가형",
                    "flower": "해바라기",
                    "personality": "INTJ",
                    "title": "용의주도한 전략가",
                    "image": "https://forour.s3.ap-northeast-2.amazonaws.com/INTJ_%E1%84%92%E1%85%A2%E1%84%87%E1%85%A1%E1%84%85%E1%85%A1%E1%84%80%E1%85%B5.svg",    
                    "kakao_image": "https://forour.s3.ap-northeast-2.amazonaws.com/INTJ_%E1%84%92%E1%85%A2%E1%84%87%E1%85%A1%E1%84%85%E1%85%A1%E1%84%80%E1%85%B5.png"
                }
            }
        }
