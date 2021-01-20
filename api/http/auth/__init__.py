"""Module contains auth & security features"""
from authlib.integrations.starlette_client import OAuth
from api.settings import SETTINGS

OAUTH = OAuth()
OAUTH.register(**SETTINGS['github'])
