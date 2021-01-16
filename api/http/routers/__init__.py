"""
Module contains HTTP Controllers/Routers for the API
"""
from . import greetings

ROUTERS = [
    greetings.router
]
