from typing import List, Optional

from fastapi import APIRouter, Query, Request, status
from fastapi.responses import JSONResponse

from src.crud import result_crud
from src.schema import (
    CreateResult,
    UpdateResult,
    create_response,
    delete_response,
    result_get_by_answers_response,
    result_get_multi_response,
    update_response,
)

router = APIRouter()


@router.get("", responses=result_get_by_answers_response)
async def get_result_by_answers(
    request: Request,
    answers: str = Query(
        ..., description="결과 조회를 위한 쿼리 파라미터", example="EEINNSFTTPPJ"
    ),
):
    """
    MBTI 질문에 대한 사용자 답변 값을 활용한 결과 개별 조회
    """
    try:
        result = await result_crud.get_one(request=request, answers=answers)

        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"data": result}
        )

    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": f"Query Parameter {answers} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.get("s", responses=result_get_multi_response)
async def get_results(
    request: Request,
    skip: int = Query(default=0, description="페이지네이션 시작 값", example=0),
    limit: int = Query(default=0, description="페이지네이션 종료 값", example=100),
    sort: Optional[List[str]] = Query(
        default=["mbti-count desc"],
        description="정렬을 위한 쿼리 파라미터",
        example="mbti+desc",
    ),
):
    """
    MBTI 질문에 대한 답변 전체 조회
    """
    try:
        result = await result_crud.get_multi(
            request=request, skip=skip, limit=limit, sort=sort
        )

        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"data": result}
        )

    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": f"Query Parameter {sort} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"deatil": error},
        )


@router.post("", responses=create_response)
async def create_result(request: Request, insert_data: CreateResult):
    """
    MBTI 질문에 대한 답변 개별 생성
    """
    try:
        result = await result_crud.create(
            request=request, insert_data=insert_data
        )

        if not result:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Database Error"},
            )

        return JSONResponse(
            status_code=status.HTTP_201_CREATED, content={"detail": "Success"}
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.put("/{result_id}", responses=update_response)
async def update_result(
    request: Request, result_id: str, update_data: UpdateResult
):
    """
    ObjectId 값을 활용한 MBTI 질문에 대한 답변 수정
    """
    try:
        result = await result_crud.update(
            request=request, id=result_id, update_data=update_data
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
            content={"detail": f"ObjectId {result_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.delete("/{result_id}", responses=delete_response)
async def delete_result(request: Request, result_id: str):
    """
    ObjectId 값을 활용한 MBTI 질문에 대한 답변 삭제
    """
    try:
        result = await result_crud.delete(request=request, id=result_id)

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
            content={"detail": f"ObjectId {result_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )
