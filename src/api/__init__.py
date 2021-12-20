from fastapi import APIRouter

from src.api import question, result, anniversary


api_router = APIRouter()

api_router.include_router(
    router=question.router,
    prefix='/question',
    tags=['Question']
)