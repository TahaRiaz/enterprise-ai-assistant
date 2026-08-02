from abc import ABC, abstractmethod

from app.database.models.chunk import Chunk

class VectorStore(ABC):

    @abstractmethod
    async def upsert(self,vectors: list[list[float]],collection_name:str,):
        ...

    @abstractmethod
    async def search(self, vector: list[float], limit: int, collection_name: str):
        ...

    @abstractmethod 
    async def create_collection(self, collection_name: str):
        ...

    @abstractmethod
    async def delete_collection(self, collection_name: str):
        ...

    @abstractmethod
    async def collection_exists(self, collection_name: str) -> bool:
        ...


    @abstractmethod
    async def delete(self,ids:int):
        ...

    