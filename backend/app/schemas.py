from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class UserIn(BaseModel):
    # TODO add password
    username: str

class UserOut(UserIn):
    id: int
    username: str
    color: str
    avatar: str
    created_at: str

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