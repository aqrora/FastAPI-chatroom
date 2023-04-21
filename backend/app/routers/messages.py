from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(
    prefix="/message",
    tags=['Messages']
)





@router.post('/message/{channel_id}')
def send_message(channel_id: int, db: Session = Depends(get_db)):
    return {"status": "ok"}


@router.get('/message/{channel_id}')
def get_messages(channel_id: int):
    return {"status": "ok"}



@router.put("/message/{channel_id}/{message_id}")
def edit_message(channel_id: int, message_id: int):
    return {"status": "ok"}