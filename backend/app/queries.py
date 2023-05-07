from sqlalchemy.orm import Session




class Query():
    def __init__(*, self, db: Session, model, id: int = None):
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

    def get_item(self):
        assert self.id is not None, "Can't find item because ID wasn't specified"
        return self.db.query(self.model).filter(self.model.id == self.id)

    def delete(self):
        self.get_item().delete(synchronize_session=False)
        self.db.commit()
