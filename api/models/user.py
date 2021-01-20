"""File contans user model"""
from pydantic import BaseModel


class User(BaseModel):
    """
    Model describing a User
    """
    uid: str
    scopes: dict
    password: str
    hashed: str

    def update_password(self, password: str):
        """Updates the user password"""
        self.password = password
