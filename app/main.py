from fastapi import FastAPI
from app.routers import greetings


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(greetings.router)

    @application.get("/")
    async def root():
        return {"message": "Hello Bigger Applications!"}

    return application


app = get_application()
