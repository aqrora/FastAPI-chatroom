from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/message",
    tags=['Messages']
)





@router.post('/{channel_id}')
def send_message(channel_id: int, db: Session = Depends(get_db)):
    return {"status": "ok"}


@router.get('/{channel_id}')
def get_messages(channel_id: int):
    return {"status": "ok"}


@router.put("/{channel_id}/{message_id}")
def edit_message(channel_id: int, message_id: int):
    return {"status": "ok"}