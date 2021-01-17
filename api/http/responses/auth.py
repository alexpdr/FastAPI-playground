"""
File contains auth response model
"""
from pydantic import BaseModel


class AuthResponse(BaseModel):
    """Auth response model"""
    access_token: str
    token_type: str
