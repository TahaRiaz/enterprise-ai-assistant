from typing import Generic, TypeVar,Type,Any
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):

    def __init__(self, db:Session, model: Type[ModelType]):
        self.db = db
        self.model = model

    def create(self, obj:ModelType):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

    def get(self, id: int):
        return self.db.get(
            self.model,
            id,
        )
    
    def update(self):
        self.db.commit()