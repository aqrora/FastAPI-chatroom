from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import database, models, utils
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from .schemas import TokenData
from typing import Union, Any
from .config import settings
from datetime import datetime, timedelta


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


class JWTToken(object):

    ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes 
    ALGORITHM = settings.algorithm
    JWT_SECRET_KEY = settings.jwt_secret_key

    def __init__(self, subject: Union[str, Any], expires_delta: int = None, refresh: bool = False):
        
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            additional_minutes = self.ACCESS_TOKEN_EXPIRE_MINUTES
            if refresh: additional_minutes = self.REFRESH_TOKEN_EXPIRE_MINUTES
            expires_delta = datetime.utcnow() + timedelta(minutes = additional_minutes)

        self.subject = subject
        self.expires_delta = expires_delta



    def create_token(self) -> str:
        
        to_encode = {"exp": self.expires_delta, "sub": str(self.subject)}
        encoded_jwt = jwt.encode(to_encode, self.JWT_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt
    
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return utils.verify_password(plain_password, hashed_password)



    @staticmethod
    def verify_token(token, credentials_exception):
        try:

            payload = jwt.decode(token, JWTToken.JWT_SECRET_KEY, algorithms=[JWTToken.ALGORITHM])
            id: str = payload.get("user_id")
            if id is None:
                raise credentials_exception
            token_data = TokenData(id=id)
        except JWTError:
            raise credentials_exception

        return token_data
    
    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):        
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        token = JWTToken.verify_token(token, credentials_exception)
        user = db.query(models.User).filter(models.User.id == token.id).first()
        return user
    