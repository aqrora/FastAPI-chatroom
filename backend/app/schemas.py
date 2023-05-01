from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    color: str
    avatar: str
    created_at: datetime

    class Config:
        orm_mode = True


class MessageIn(BaseModel):
    message_text: str
    by_user_id: int
    channel_id: int

class MessageOut(MessageIn):
    id: int
    created_at: datetime
    edited: bool

    
    class Config:
        orm_mode = True

class ChannelIn(BaseModel):
    title: str
    owner: int

class ChannelOut(ChannelIn):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None