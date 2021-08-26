import uvicorn

from fastapi                   import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core                  import project_settings


server = FastAPI(title=project_settings.TITLE)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:server",
        host = "0.0.0.0",
        port = 80,
        reload = True
    )