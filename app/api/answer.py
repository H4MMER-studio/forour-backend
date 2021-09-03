import traceback

from fastapi           import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.crud          import answer
from app.schemas       import AnswerCreate, AnswerUpdate
from app.database      import get_session


router = APIRouter()


@router.get("/{question_id}")
def get_answer_by_question_id(question_id: int, db=Depends(get_session)):
    pass


@router.get("")
def get_answers(db=Depends(get_session)):
    try:
        data = answer.get_all(db=db)
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
def create_answer(obj_in: AnswerCreate, db=Depends(get_session)):
    try:
        data = answer.create(db=db, obj_in=obj_in)
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