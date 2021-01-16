"""
File contains greet model
"""
from pydantic import BaseModel


class GreetResponse(BaseModel):
    """Greetings Reponse Model"""
    greeting: str
