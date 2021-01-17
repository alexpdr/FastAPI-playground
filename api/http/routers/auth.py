"""
File contains endpoint router for /auth/ endpoints
"""
from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2AuthorizationCodeBearer
from api.http.responses.auth import AuthResponse
from api.http.auth import Session

router = APIRouter(
    tags=["Auth"]
)


@router.post(
    path='/token',
    operation_id="api.routers.auth.login",
    response_model=AuthResponse,
    response_description="Successfully greeted the authenticated name",
    status_code=200)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """Attenpts to athenticate the user session"""
    session: Session = Session(
        username=form.username,
        password=form.password
    )
    return {"access_token": session.generate_token(), "token_type": "bearer"}

@router.post(
    path='/github',
    operation_id="api.routers.auth.bearer",
    response_model=AuthResponse,
    response_description="Successfully greeted the authenticated name",
    status_code=200)
async def github(bearer: OAuth2AuthorizationCodeBearer = Depends()):
    """Attenpts to athenticate the user session"""
    session: Session = Session(
        username=form.username,
        password=form.password
    )
    return {"access_token": session.generate_token(), "token_type": "bearer"}