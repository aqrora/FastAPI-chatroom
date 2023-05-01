from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import schemas, database, models
from jose import JWTError, jwt
from .schemas import TokenData
from typing import Union, Any
from .config import settings
import requests
import random


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

class Generate():
     
    @staticmethod
    def random_color():
        # Generates random hex value for the color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)

    @staticmethod
    def random_cat():
        # Generates link to random cat picture
        try:
            response = requests.get("https://api.thecatapi.com/v1/images/search", timeout=5)
            return response.json()[0]['url']
        except Exception as e: # Api is down
            print(e)
            return "https://miramarvet.com.au/wp-content/uploads/2021/08/api-cat2.jpg"


    @staticmethod
    def hashed_password(password: str) -> str:
        return password_context.hash(password)




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
        return password_context.verify(plain_password, hashed_password)



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

        token = JWTToken.verify_access_token(token, credentials_exception)

        user = db.query(models.User).filter(models.User.id == token.id).first()

        return user