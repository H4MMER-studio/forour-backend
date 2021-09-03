from fastapi import APIRouter

from app.api import question
from app.api import answer
from app.api import result


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
api_router.include_router(
    router = result.router,
    prefix = "/results",
    tags   = ["results"]
)