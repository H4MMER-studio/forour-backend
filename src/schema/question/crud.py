from pydantic import BaseModel


class QuestionBase(BaseModel):
    question: str | None
    question_order: int | None
    answers: list[dict[str, int | str]] | None


class CreateQuestion(QuestionBase):
    question: str
    question_order: int
    answers: list[dict[str, int | str]]

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
