from sqlalchemy.orm import Session
from fastapi import status, HTTPException



class Query():
    def __init__(self, db: Session, model, id: int = None):
        self.db = db
        self.model = model
        self.id = None
        if id is not None:
            self.id = id


    def create(self, **kwargs):
        new_model = self.model(**kwargs)
        self.db.add(new_model)
        self.db.commit()
        self.db.refresh(new_model)
        return new_model

    def get_item(self): # (returns query)
        assert self.id is not None, "Can't find item because ID wasn't specified"
        return self.db.query(self.model).filter(self.model.id == self.id)


    def generate_notfound_exception(self):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{self.model.__tablename__[:-1].title()} with id: {self.id} does not exist")
        

    def validate_existance(self):
        if not self.get_item().first():
            self.generate_notfound_exception()

    def delete(self):
        self.validate_existance()

        self.get_item().delete(synchronize_session=False)
        self.db.commit()
