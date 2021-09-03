from app.schemas.response import SuccessResponseBase


class GetQuestionResponse(SuccessResponseBase):
    
    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "Question": {
                        "content": "name의 어떤 부분이 좋았어요?",
                        "id": 2
                    },
                    "Answer": {
                        "content_b": {
                            "content": "한 명, 한 명 배려해주는 세심함이 좋았어요.",
                            "personality": "I"
                        },
                        "question_id": 2,
                        "content_a": {
                            "content": "다른 사람들 앞에서 자신감 있는 모습이 좋았어요.",
                            "personality": "E"
                        },
                        "id": 2
                    }
                }
            }
        }


class GetQuestionsResponse(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": [
                    {
                        "Question": {
                            "content": "처음에 둘은 어떻게 친해졌나요?",
                            "id": 1
                        },
                        "Answer": {
                            "question_id": 1,
                            "content_a": {
                                "content": "name이(가) 먼저 제가 말을 걸어줬어요.",
                                "personality": "E"
                            },
                            "id": 1,
                            "content_b": {
                                "content": "제가 name에게 먼저 말을 걸었어요.",
                                "personality": "I"
                            }
                        }
                    },
                    {
                        "Question": {
                            "content": "name의 어떤 부분이 좋았어요?",
                            "id": 2
                        },
                        "Answer": {
                            "question_id": 2,
                            "content_a": {
                                "content": "다른 사람들 앞에서 자신감 있는 모습이 좋았어요.",
                                "personality": "E"
                            },
                            "id": 2,
                            "content_b": {
                                "content": "한 명, 한 명 배려해주는 세심함이 좋았어요.",
                                "personality": "I"
                            }
                        }
                    }
                ]
            }
        }