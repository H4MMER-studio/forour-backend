import uvicorn

from fastapi                 import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api                 import api_router
from app.core                import project_settings
from app.database            import create_db_and_tables


server = FastAPI(title=project_settings.TITLE)

server.include_router(router=api_router, prefix=project_settings.COMMON_API)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://forour.space",
    "https://forour.space"
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@server.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run(
        "app.main:server",
        host = "0.0.0.0",
        port = 8000,
        reload = True
    )