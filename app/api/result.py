import traceback

from fastapi           import APIRouter, status, Depends, Body
from fastapi.responses import JSONResponse

from app.crud          import result
from app.models        import Personality
from app.schemas       import (
                        ResultCreate,
                        ResultUpdate,
                        GetResultResponse
                        )
from app.database      import get_session


router = APIRouter()


@router.get("", response_model=GetResultResponse)
def get_result(mbti: Personality, db=Depends(get_session)):
    try:
        data = result.get(db=db, mbti=mbti)
        if data:
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content = {"data": data}
            )
        else:
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content = {"detail": "The result was not found"}
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


@router.patch("/{id}")
def update_result(obj_in: ResultUpdate, db=Depends(get_session)):
    try: 
        data = result.update(db=db, obj_in=obj_in)
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