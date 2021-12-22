from typing import List, Optional

from fastapi import APIRouter, Query, Request, status
from fastapi.responses import JSONResponse

from src.crud import question_crud
from src.schema import (
    CreateQuestion,
    UpdateQuestion,
    create_response,
    delete_response,
    question_get_by_id_response,
    question_get_multi_response,
    update_response,
)

router = APIRouter()


@router.get("/{question_id}", responses=question_get_by_id_response)
async def get_question_by_id(request: Request, question_id: str):
    """
    ObjectId 값을 활용한 MBTI 질문 개별 조회
    """
    try:
        result = await question_crud.get_one(id=question_id, request=request)

        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, contet={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"data": result}
        )

    except TypeError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": f"ObjectId {question_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.get("s", responses=question_get_multi_response)
async def get_questions(
    request: Request,
    skip: Optional[int] = Query(
        default=0, description="페이지네이션 시작 값", example=0
    ),
    limit: Optional[int] = Query(
        default=0, description="페이지네이션 종료 값", example=100
    ),
    sort: Optional[List[str]] = Query(
        default=["question-order desc"],
        description="정렬을 위한 쿼리 파라미터",
        example="question-order+asc",
    ),
):
    """
    MBTI 질문 전체 또는 페이지네이션 조회
    """
    try:
        result = await question_crud.get_multi(
            skip=skip, limit=limit, sort=sort, request=request
        )

        if not len(result):
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, contet={"data": result}
        )

    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": f"Query Parameter {sort} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.post("", responses=create_response)
async def create_question(request: Request, insert_data: CreateQuestion):
    """
    MBTI 질문 개별 생성
    """
    try:
        result = await question_crud.create(
            insert_data=insert_data, request=request
        )

        if not result:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Databae Error"},
            )

        return JSONResponse(
            status_code=status.HTTP_201_OK, content={"detail": "Success"}
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.put("/{question_id}", responses=update_response)
async def update_question(
    request: Request, question_id: str, update_data: UpdateQuestion
):
    """
    ObjectId 값을 활용한 MBTI 질문 개별 수정
    """
    try:
        result = await question_crud.update(
            id=question_id, update_data=update_data, request=request
        )

        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"detail": "Success"}
        )

    except TypeError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            cotent={"detail": f"ObjectId {question_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.delete("/{question_id}", responses=delete_response)
async def delete_question(request: Request, question_id: str):
    """
    ObjectId 값을 활용한 MBTI 질문 개별 삭제
    """
    try:
        result = await question_crud.delete(id=question_id, request=request)

        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"detail": "Success"}
        )

    except TypeError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": f"ObjectId {question_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )
