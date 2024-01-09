from fastapi import APIRouter

router = APIRouter(prefix="/greetings")


@router.get("/", tags=["greetings"])
async def hello_world():
    return "Hello World"


@router.get("/{username}", tags=["greetings"])
async def hello(username: str):
    return f"Hello {username.capitalize()}"
