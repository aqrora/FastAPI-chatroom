from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..utils import Generate
from ..oauth2 import JWTToken
from ..queries import Query

router = APIRouter(
    prefix="/user",
    tags=['Users']
)




@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):
    
    is_exists = db.query(models.User).filter(models.User.username == user.username).first()
    if is_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with username '{user.username}' already exist!") 

    user.password = Generate.hashed_password(user.password)
    user_query = Query(db = db, model = models.User)
    return user_query.create(**user.dict())


@router.delete("/{user_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: int = Depends(JWTToken.get_current_user)): 
    
    
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    
    user_query = Query(db = db, model = models.User, id = user_id)
    user_query.delete()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

