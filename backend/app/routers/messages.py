from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from ..oauth2 import JWTToken

router = APIRouter(
    prefix="/message",
    tags=['Messages']
)




# TODO ratelimit
@router.post('/{channel_id}', response_model=schemas.MessageOut)
def send_message(channel_id: int, message: schemas.MessageIn, current_user: int = Depends(JWTToken.get_current_user), 
                 db: Session = Depends(get_db)):
    # TODO websocket call
    msg = models.Message(message_text = message.text, by_user_id = current_user.id, 
                         channel_id = channel_id)
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return msg


@router.get('/{channel_id}', response_model=List[schemas.MessageOut])
def get_messages(channel_id: int, db: Session = Depends(get_db)):
    channel = db.query(models.Channel).filter(
        models.Channel.id == channel_id
        ).first()
    
    if not channel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Channel with id: {channel_id} does not exist")
    messages = db.query(models.Message).filter(models.Message.channel_id == channel_id).all()

    return {"messages": messages}



@router.put("/{channel_id}/{message_id}", response_model=schemas.MessageOut)
def update_message(channel_id: int, message_id: int, updated_message: schemas.MessageIn,
                   current_user: int = Depends(JWTToken.get_current_user), db: Session = Depends(get_db)):
    # TODO websocket call
    message_query = db.query(models.Message).filter(models.Message.id == message_id)

    message = message_query.first()

    if message == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with id: {message_id} does not exist")
    if message.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    message.message_text = updated_message.message_text
    message.edited = True
    db.commit()

    return message_query.first()
