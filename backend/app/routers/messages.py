from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..oauth2 import JWTToken
from ..queries import Query
from typing import List

router = APIRouter(
    prefix="/message",
    tags=['Messages']
)




# TODO ratelimit
@router.post('/{channel_id}', response_model=schemas.MessageOut)
def send_message(channel_id: int, message: schemas.MessageIn, current_user: int = Depends(JWTToken.get_current_user), 
                 db: Session = Depends(get_db)):
    # TODO websocket call
    message_query = Query(db = db, model = models.Message)

    return message_query.create(message_text = message.text, by_user_id = current_user.id, 
                         channel_id = channel_id)


@router.get('/{channel_id}', response_model=List[schemas.MessageOut])
def get_messages(channel_id: int, db: Session = Depends(get_db)):
    channel_query = Query(db = db, model = models.Channel, id = channel_id)
    channel_query.validate_existance()

    messages = db.query(models.Message).filter(models.Message.channel_id == channel_id).all()

    return {"messages": messages}






@router.put("/{message_id}", response_model=schemas.MessageOut)
def update_message(message_id: int, updated_message: schemas.MessageIn,
                   current_user: int = Depends(JWTToken.get_current_user), db: Session = Depends(get_db)):
    # TODO websocket call
    message_query = Query(db = db, model = models.Message, id = message_id)
    message = message_query.get_item().first()

    message_query.validate_existance() # Returns 404 if message with this id does not exists

    if message.by_user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    message.message_text = updated_message.message_text
    message.edited = True
    db.commit()

    return message_query.first()


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(message_id: int, current_user: int = Depends(JWTToken.get_current_user), 
                   db: Session = Depends(get_db)):

    message_query = Query(db = db, model = models.Message, id = message_id)
    message = message_query.first()
    if message.by_user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    message_query.delete()

    return Response(status_code=status.HTTP_204_NO_CONTENT)