from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/channel",
    tags=['Channels']
)


@router.post('/{channel_id}')
def create_channel(channel_id: int, db: Session = Depends(get_db)):
    return {"status": "ok"}



@router.delete('/{channel_id}')
def delete_channel(channel_id: int, db: Session = Depends(get_db)):
    return {"status": "ok"}
