from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..utils import Generate

router = APIRouter(
    prefix="/user",
    tags=['Users']
)




@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):
    # Check for username in database (is exists)
    is_exists = db.query(models.User).filter(models.User.username == user.username).first()
    if is_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with username '{user.username}' already exist!") 

    user.password = Generate.hashed_password(user.password)
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.delete("/{user_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)): 

    # TODO Check for current user, check user.id == id
    
    user_query = db.query(models.User).filter(models.User.id == user_id)
    user = user_query.first()
    if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user_id} does not exist")
    user_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

