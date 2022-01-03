from src.schema.response import AlterResponseModel

create_response_example = {
    "200": {
        "model": AlterResponseModel,
        "description": "성공",
        "content": {"application/json": {"example": {"detail": "Success"}}},
    }
}
