from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class GetResponseModel(BaseModel):
    data: Optional[Union[List[dict], Dict[str, Union[str, int]]]]


class AlterResponseModel(BaseModel):
    detail: str


class ErrorResponseModel(BaseModel):
    detail: Union[str, List[Dict[str, str]]]
