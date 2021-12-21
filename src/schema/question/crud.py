from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class QuestionBase(BaseModel):
    question: str
    question_order: int
    answers: List[Dict[str, Union[int, str]]]


class CreateQuestion(QuestionBase):
    class Config:
        schema_extra = {
            "example": {
                "question": "처음에 둘은 어떻게 친해졌나요?",
                "question_order": 1,
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


class UpdateQuestion(QuestionBase):
    question: Optional[str]
    question_order: Optional[int]
    answers: Optional[List[Dict[str, Union[int, str]]]]

    class Config:
        schema_extra = {
            "example": {
                "answers": [
                    {
                        "id": 1,
                        "content": "우리 자주 보자! 내일도 연락해.",
                        "personality": "N",
                    }
                ]
            }
        }
