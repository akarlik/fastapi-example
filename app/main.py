from fastapi import FastAPI, Request
from app.routers import greetings
from app.utils import logger


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(greetings.router)
    application_logger = logger.Logger.make_logger()
    application.logger = application_logger

    @application.get("/")
    async def root(request: Request):
        request.app.logger.info("!!!!!!!!!")
        return {"message": "Hello Bigger Applications!"}

    return application


app = get_application()
