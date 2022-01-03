import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from src.api import api_router
from src.core import get_settings

app = FastAPI(
    title=get_settings().PROJECT_TITLE,
    description=get_settings().PROJECT_DESCRIPTION,
    version=get_settings().PROJECT_VERSION,
)


@app.on_event("startup")
async def connect_db():
    app.db_client = AsyncIOMotorClient(get_settings().DB_URL)
    app.db = app.db_client[get_settings().DB_NAME]


@app.on_event("shutdown")
async def close_db():
    app.db_client.close()


app.include_router(router=api_router, prefix=get_settings().COMMON_API)


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=get_settings().HOST,
        port=get_settings().PORT,
        reload=get_settings().RELOAD,
    )
