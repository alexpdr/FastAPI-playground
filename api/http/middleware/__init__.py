"""Module contains http middleware"""
from starlette.middleware.sessions import SessionMiddleware

MIDDLEWARE = [
    SessionMiddleware
]
