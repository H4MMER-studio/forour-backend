from fastapi import APIRouter

from app.api import question


api_router = APIRouter(prefix="/v1")

api_router.include_router(
    router  = question.router,
    prefix  = "/question",
    tags    = ["question"]
)