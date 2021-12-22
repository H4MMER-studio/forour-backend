from typing import List, Optional

from fastapi import APIRouter, Query, Request, status
from fastapi.responses import JSONResponse

from src.crud import anniversary_crud
from src.schema import (
    CreateAnniversary,
    UpdateAnniversary,
    anniversary_get_by_id_response,
    anniversary_get_multi_response,
    create_response,
    delete_response,
    update_response,
)

router = APIRouter()


@router.get("/{anniversary_id}", responses=anniversary_get_by_id_response)
async def get_anniversary_by_id(anniversary_id: str, request: Request):
    """
    ObjectId 값을 활용한 기념일 개별 조회
    """
    try:
        result = await anniversary_crud.get_by_id(
            id=anniversary_id, request=request
        )

        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"detail": result}
        )

    except TypeError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": f"ObjectId {anniversary_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.get("s", responses=anniversary_get_multi_response)
async def get_anniversaries(
    request: Request,
    skip: Optional[int] = Query(
        default=0, description="페이지네이션 시작 값", example=0
    ),
    limit: Optional[int] = Query(
        default=0, description="페이지네이션 종료 값", example=100
    ),
    sort: Optional[List[str]] = Query(None),
):
    """
    기념일 전체 또는 페이지네이션 조회
    """
    try:
        result = await anniversary_crud.get_multi(
            request=request, skip=skip, limit=limit, sort=None
        )

        if not len(result):
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content={"data": []}
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"data": result}
        )

    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": f"Query Pararmeter {sort} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.post("", responses=create_response)
async def create_anniversary(request: Request, insert_data: CreateAnniversary):
    """
    기념일 생성
    """
    try:
        result = await anniversary_crud.create(
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


@router.put("/{anniversary_id}", responses=update_response)
async def update_anniversary(
    anniversary_id: str, request: Request, update_data: UpdateAnniversary
):
    """
    ObjectId 값을 활용한 기념 개별 수정
    """
    try:
        result = await anniversary_crud.update(
            request=request, id=anniversary_id, update_data=update_data
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
            content={"detail": f"ObjectId {anniversary_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )


@router.delete("/{anniversary_id}", responses=delete_response)
async def delete_anniversary(anniversary_id: str, request: Request):
    """
    ObjectId 값을 활용한 기념일 개별 삭제
    """
    try:
        result = await anniversary_crud.delete(
            id=anniversary_id, request=request
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
            content={"detail": f"ObjectId {anniversary_id} Invalid"},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error},
        )
