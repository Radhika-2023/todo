from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from app.env import JWT_SECRET_KEY, ALGORITHM
from database import get_db_session
from common.exceptions import JsonException

db = Annotated[Session, Depends(get_db_session)]

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise JsonException(state=False,response="Invalid Auth Scheme",message="Auth scheme is not Bearer",status=status.HTTP_403_FORBIDDEN)
            if not self.verify_jwt(credentials.credentials):
                raise JsonException(state=False,response="Invalid Token",message="Invalid access token or expired token",status=status.HTTP_401_UNAUTHORIZED)
            return credentials.credentials
        else:
            raise JsonException(state=False,response="Invalid Token",message="Could not validate credentials",status=status.HTTP_403_FORBIDDEN)

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = jwt.decode(
                jwtoken, JWT_SECRET_KEY, algorithms=[ALGORITHM]
            )
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid

