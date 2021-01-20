"""File contains token model"""
from pydantic import BaseModel
from datetime import datetime


class Token(BaseModel):
    """
    Model describing a User Access Token
    """
    uid: str
    scopes: dict
    expiry: datetime

    def claims(self):
        """Returns claim"""
        return {
            'sub': self.uid,
            'scopes': self.scopes,
            'exp': self.expiry
        }