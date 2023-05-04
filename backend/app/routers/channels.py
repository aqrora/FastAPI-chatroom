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
    channel = models.Channel(**channel.dict())
    db.add(channel)
    db.commit()
    db.refresh(channel)
    return channel



@router.delete('/{channel_id}')
def delete_channel(channel_id: int, current_user: int = Depends(JWTToken.get_current_user), 
                   db: Session = Depends(get_db)):
    channel_query = db.query(models.Channel).filter(models.Channel.id == channel_id)
    channel = channel_query.first()

    if channel == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Channel with id: {channel_id} does not exist")
    if channel.owner != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    channel_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
