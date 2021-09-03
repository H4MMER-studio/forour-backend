from app.crud.base    import CRUDBase
from app.models       import Result
from app.schemas      import ResultCreate, ResultUpdate


class CRUDResult(CRUDBase[Result, ResultCreate, ResultUpdate]):
    pass

result = CRUDResult(Result)