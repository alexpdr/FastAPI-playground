"""
Module contains HTTP Controllers/Routers for the API
"""
from . import greetings
from . import auth

ROUTERS = [
    greetings.router,
    auth.router
]
