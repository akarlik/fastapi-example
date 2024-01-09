from fastapi import FastAPI
from app.routers import greetings

app = FastAPI()
app.include_router(greetings.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
