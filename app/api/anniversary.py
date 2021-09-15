import traceback

from fastapi           import APIRouter, status, Depends, Body
from fastapi.responses import JSONResponse

from app.crud          import anniversary
from app.models        import AnniversaryType
from app.schemas       import (
                        AnniversaryCreate,
                        AnniversaryUpdate,
                        GetAnniversary,
                        GetAnniversaries
                        )
from app.database      import get_session


router = APIRouter()


@router.get("/{type}", response_model=GetAnniversary)
def get_anniversary(type: AnniversaryType, db=Depends(get_session)):
    try:
        data = anniversary.get(db=db, anniversary=type)
        if data:
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content = {"data": data}
            )
        else:
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content = {"detail": "The anniversary was not found"}
            )

    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {"detail": f"server error: {error}"}
        )


@router.get("", response_model=GetAnniversaries)
def get_anniversaries(db=Depends(get_session)):
    try:
        data = anniversary.get_all(db=db)
        if data:
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content     = {"data": data}
            )
        else:
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content     = {"detail": "The anniversaries were not found"}
            )

    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content     = {"detail": f"server error: {error}"}
        )


@router.post("")
def create_anniversary(obj_in: AnniversaryCreate, db=Depends(get_session)):
    try:
        data = anniversary.create(db=db, obj_in=obj_in)
        return JSONResponse(
            status_code = status.HTTP_200_OK,
            content = {"data": data}
        )

    except Exception as error:
        print(traceback.print_exc())
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {"detail": f"server error: {error}"}
        )
