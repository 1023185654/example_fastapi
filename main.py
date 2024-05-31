import uvicorn
from fastapi import FastAPI

from app import view
from app.utils.logger import Logging

t_app = FastAPI()
t_app.include_router(view.router, prefix="/v1")

if __name__ == "__main__":
    Logging()
    uvicorn.run("main:t_app", host="0.0.0.0", port=9000, reload=True)
