from src.schema.response import ErrorResponseModel, GetResponseModel

result_get_by_answers_response = {
    "200": {
        "model": GetResponseModel,
        "description": "성공",
        "content": {
            "application/json": {
                "example": {
                    "data": {
                    }
                }
            }
        },
    },
    "404": {
        "model": GetResponseModel,
        "description": "존재하지 않는 엔티티",
        "content": {"application/json": {"example": {"data": []}}},
    },
    "422": {
        "model": ErrorResponseModel,
        "description": "유효하지 않은 매개변수 사용",
        "content": {
            "application/json": {
                "example": {
                        "detail": "Query Parameter IIIABCDEFZDS Invalid"
                    }
                }
            }
    }
}
