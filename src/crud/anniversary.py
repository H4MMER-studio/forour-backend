from src.crud.base import CRUDBase
from src.schema import CreateAnniversary, UpdateAnniversary


class CRUDAnniversary(CRUDBase[CreateAnniversary, UpdateAnniversary]):
    pass


anniversary_crud = CRUDAnniversary(collection="anniversaries")
