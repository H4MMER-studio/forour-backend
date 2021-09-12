from app.crud.base import CRUDBase
from app.models    import Anniversary
from app.schemas   import AnniversaryCreate, AnniversaryUpdate


class CRUDAnniversary(CRUDBase[Anniversary, AnniversaryCreate, AnniversaryUpdate]):
    pass


anniversary = CRUDAnniversary(Anniversary)