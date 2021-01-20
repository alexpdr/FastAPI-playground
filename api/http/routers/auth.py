"""
File contains endpoint router for /auth/ endpoints
"""
from fastapi import APIRouter
from fastapi import Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2AuthorizationCodeBearer
from authlib.integrations.starlette_client import OAuth
from api.http.responses.auth import AuthResponse
from api.http.auth import OAUTH


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.get(
    path='/github',
    operation_id='auth.github',
    response_description="Authorize redirect to GitHub")
async def login_via_github(request: Request):
    return await OAUTH.github.authorize_redirect(request)

@router.get(
    path='/github/success',
    operation_id='auth.github.success',
    response_description="Successfully authorized with GitHub")
async def authorize_github(request: Request):
    token = await OAUTH.github.authorize_access_token(request)
    request.session['token'] = await dict(token)
    return RedirectResponse(url='/docs')


# Internal session method TODO: re-eval
# @router.post(
#     path='/token',
#     operation_id="api.routers.auth.login",
#     response_model=AuthResponse,
#     response_description="Successfully greeted the authenticated name",
#     status_code=200)
# async def login(form: OAuth2PasswordRequestForm = Depends()):
#     """Attenpts to athenticate the user session"""
#     session: Session = Session(
#         username=form.username,
#         password=form.password
#     )
#     return {"access_token": session.generate_token(), "token_type": "bearer"}


