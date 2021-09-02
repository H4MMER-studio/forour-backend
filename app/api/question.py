import traceback

from fastapi           import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.crud          import question
from app.schemas       import QuestionCreate, QuestionUpdate
from app.database      import get_session


router = APIRouter()

@router.get("/{id}")
def get_qustion(id: int, db=Depends(get_session)):
    try:
        data = question.get(db=db, id=id)
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


@router.get("")
def get_questions(db=Depends(get_session)):
    try:
        data = question.get_all(db=db)
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
def create_question(obj_in: QuestionCreate, db=Depends(get_session)):
    try:
        data = question.create(db=db, obj_in=obj_in)
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
def update_question(id: int, obj_in: QuestionUpdate, db=Depends(get_session)):
    try:
        data = question.update(db=db, id=id, obj_in=obj_in)
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
def delete_question(id: int, db=Depends(get_session)):
    try:
        data = question.remove(db=db, id=id)
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