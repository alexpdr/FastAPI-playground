"""
Module contains Auth functionality for the API
"""
from typing import List, Union
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError, jwt
from api.settings import SETTINGS
from pydantic import BaseModel, ValidationError
from passlib.context import CryptContext
from api.models import Token, User

# TODO: Re-eval this file
SCHEMA = OAuth2PasswordBearer(
    tokenUrl=SETTINGS['AUTH']['token_url'],
    scopes=SETTINGS['AUTH']['scopes'],
)


admin_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
admin = User(
    uid="1234",
    password="1234",
    scopes=SETTINGS['AUTH']['scopes'],
    hashed=str(admin_context.hash("1234"))
)

fake_db = {
    "admin": admin
}

class Session:
    """Auth Session object"""
    username: Union[str]
    password: Union[str]
    schema: Union[list]
    encoded: Union[str]
    expiry: timedelta
    algorithm: Union[List[str], str]
    context: Union[CryptContext]

    def __init__(self, **kwargs):
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.schema = kwargs.get('schema', None)
        self.encoded = kwargs.get('encoded', None)
        self.expiry = timedelta(minutes=SETTINGS['AUTH']['expiry'])
        self.algorithm = SETTINGS['AUTH']['algorithm']
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        if kwargs.get('authenticate', None):
            self._authenticate()

    def _hash(self):
        """Returns the hashed password"""
        return self.context.hash(self.password)

    def _decode(self) -> Token:
        """Attempts to decode the inbound credentials"""
        try:
            token: Token = jwt.decode(
                token=self.encoded,
                key=self.password,
                algorithms=self.algorithm
            )
            if not token:
                HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid credentials",
                )
            elif 'uid' not in token.keys():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid credentials",
                )
            elif 'scopes' not in token.keys():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid scopes"
                )
            else:
                return token
        except (JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

    def _user(self):
        """Returns the _user"""
        # self._decode()
        return fake_db.get('admin', None)  # TODO: DB

    def _authenticate(self) -> Union[User, None]:
        """Attempts to authenticate the _user"""
        _user = self._user()
        if not _user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing or invalid credentials",
            )
        elif not self.context.verify(_user.password, _user.hashed):
            raise HTTPException(
                status_code=400,
                detail="Incorrect username or password"
            )
        else:
            return _user

    def authorize(self) -> object:
        # """Attempts to authorize the _user"""
        _user = self._authenticate()
        if _user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized"
            )

        for scope in self.schema.scopes:
            if scope not in _user.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Insufficient permissions granted by scope"
                )

        return _user

    def generate_token(self) -> str:
        """Attempts to create a new JWT"""
        _user = self._authenticate()
        token = Token(
            uid=_user.uid,
            scopes=_user.scopes,
            expiry=datetime.utcnow() + self.expiry
        )  # TODO: DB
        return jwt.encode(
            claims=token.claims(),
            key=SETTINGS['AUTH']['secret'],
            algorithm=self.algorithm
        )


def session(schema: SecurityScopes, token: str = Depends(SCHEMA)):
    """Checks to see if the session_user is authorized to use this resource"""
    session = Session(encoded=token, schema=schema)
    return session.authorize()
