from app.schemas.response import SuccessResponseBase


class GetResultResponse(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    
                }
            }
        }
