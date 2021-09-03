from app.schemas.response import SuccessResponseBase


class GetResultsResponse(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": [

                ]
            }
        }
