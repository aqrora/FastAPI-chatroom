from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..oauth2 import JWTToken
from typing import List

router = APIRouter(
    prefix="/channel",
    tags=['Channels']
)





@router.get('/', response_model=List[schemas.ChannelOut])
def get_channels(current_user: int = Depends(JWTToken.get_current_user), 
                 db: Session = Depends(get_db)):
    channels = db.query(models.Channel).all()
    return {'channels': channels}



@router.post('/', response_model=schemas.ChannelOut)
def create_channel(channel: schemas.ChannelIn, current_user: int = Depends(JWTToken.get_current_user),
                   db: Session = Depends(get_db)):
    # TODO validation
    channel_query = Query(db = db, model = models.Channel)
    
    return channel_query.create(**channel.dict())



@router.delete('/{channel_id}')
def delete_channel(channel_id: int, current_user: int = Depends(JWTToken.get_current_user), 
                   db: Session = Depends(get_db)):
    channel_query = Query(db = db, model = models.Channel, id = channel_id)
    channel = channel_query.first()
    if channel.owner != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    channel_query.delete()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
