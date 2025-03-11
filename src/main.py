from fastapi import FastAPI
import uvicorn

from src.config import settings
from src.router import router as api_router


app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )
