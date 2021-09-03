from fastapi import APIRouter

from app.api import question
from app.api import answer


api_router = APIRouter(prefix="/v1")

api_router.include_router(
    router  = question.router,
    prefix  = "/questions",
    tags    = ["questions"]
)
api_router.include_router(
    router = answer.router,
    prefix = "/answers",
    tags   = ["answers"]
)