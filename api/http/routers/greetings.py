"""
File contains endpoint routerController for /hello/
"""
from fastapi import APIRouter, Response
from api.http.responses.greet import GreetResponse

router = APIRouter(
    prefix="/greetings",
    tags=["Greetings"]
)


@router.get(
    path='/greet/{name}',
    operation_id="api.greetings.greet",
    response_model=GreetResponse,
    response_description="Successfully greeted the name",
    status_code=200)
async def greet(name: str) -> Response:
    """
    Endpoint provides a gretting to the provided name
    """
    return {"greeting": f"Hello {name}!"}
