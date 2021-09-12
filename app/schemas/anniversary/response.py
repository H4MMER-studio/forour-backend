from app.schemas.response import SuccessResponseBase


class GetAnniversaries(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": [

                ]
            }
        }


class GetAnniversary(SuccessResponseBase):

    class Config:
        schema_extra = {
            "example": {
                "data": {

                }
            }
        }