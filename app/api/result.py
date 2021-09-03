import traceback

from fastapi           import APIRouter, status, Depends, Query
from fastapi.responses import JSONResponse

from app.crud          import result
from app.schemas       import (
                        ResultCreate,
                        GetResultsResponse
                        )
from app.database      import get_session


router = APIRouter()

@router.get("/{id}", response_model=GetResultsResponse)
def get_result(id: int, db=Depends(get_session)):
    try:
        data = result.get(db=db, id=id)
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


@router.post("")
def create_result(obj_in: ResultCreate, db=Depends(get_session)):
    try:
        data = result.create(db=db, obj_in=obj_in)
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


@router.delete("/{id}")
def delete_result(id: int, db=Depends(get_session)):
    try:
        data = result.remove(db=db, id=id)
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