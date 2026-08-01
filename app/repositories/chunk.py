from app.repositories.base import BaseRepository

from app.database.models.chunk import Chunk

class ChunkRepository(BaseRepository):


    def __init__(self, db):
        super().__init(db,Chunk)


    def create_many(self, objects: list[Chunk]):

        self.db.add_all(objects)
        self.db.commit()


        for obj in objects:
            self.db.refresh(obj)

        return objects