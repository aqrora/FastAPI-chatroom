from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from . import utils



class Channel(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(32), default="No theme", nullable=False)
    owner = Column(Integer, ForeignKey("users.id"), nullable=False) # Id of user who created this channel

    user = relationship("User", backref="channels")
    messages = relationship("Message", back_populates="channel")
    

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    color = Column(String(7), nullable=False, default = '#000000')
    avatar = Column(String, nullable=False, default="https://miramarvet.com.au/wp-content/uploads/2021/08/api-cat2.jpg")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    messages = relationship("Message", back_populates="user")
    
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.color = utils.Generate.random_color()
        self.avatar = utils.Generate.random_cat()


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, nullable=False)
    message_text = Column(String(255), nullable=False)
    by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    channel_id = Column(Integer, ForeignKey("channels.id"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    edited = Column(Boolean, nullable=False, default=False)
    
    user = relationship("User", back_populates="messages")
    channel = relationship("Channel", back_populates="messages")

    def __init__(self, message_text: str, by_user_id: int, channel_id: int):
        self.message_text = message_text
        self.by_user_id = by_user_id
        self.channel_id = channel_id
        
