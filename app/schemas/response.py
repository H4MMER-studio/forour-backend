from typing   import Union

from pydantic import BaseModel


class SuccessResponseBase(BaseModel):
    data: Union[list, dict, None]

    class Config:
        schema_extra = {
            "example": {
                "data": ""
            }
        }