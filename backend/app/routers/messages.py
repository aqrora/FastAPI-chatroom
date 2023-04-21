from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/message",
    tags=['Messages']
)





@router.post('/{channel_id}')
def send_message(channel_id: int, db: Session = Depends(get_db)):
    return {"status": "ok"}


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


@router.put("/{channel_id}/{message_id}")
def edit_message(channel_id: int, message_id: int):
    return {"status": "ok"}