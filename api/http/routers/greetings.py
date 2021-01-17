"""
File contains endpoint routerController for /hello/
"""
from fastapi import APIRouter, Response, Security
from api.http.responses.greet import GreetResponse
from api.http.auth import User, session


router = APIRouter(
    prefix="/greetings",
    tags=["Greetings"]
)


@router.get(
    path='/greet/{name}',
    operation_id="api.routers.greetings.greet",
    response_model=GreetResponse,
    response_description="Successfully greeted the name",
    status_code=200)
async def greet(name: str) -> Response:
    """
    Endpoint provides a gretting to the provided name
    """
    return {"greeting": f"Hello {name}!"}


@router.get(
    path='/authoried_greet/{name}',
    operation_id="api.greetings.authoried_greet",
    response_model=GreetResponse,
    response_description="Successfully greeted the name",
    status_code=200)
async def authoried_greet(
        name: str,
        user: User = Security(session, scopes=["authorized"])) -> Response:
    """
    Endpoint provides a gretting to the provided name
    """
    return {"greeting": f"Hello {name}!"}
