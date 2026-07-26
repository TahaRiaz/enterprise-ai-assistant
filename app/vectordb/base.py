from abc import ABC, abstractmethod

class VectorStore(ABC):

    @abstractmethod
    async def upsert(self, vectors):
        ...

    @abstractmethod
    async def search(self, vector,limit:int):
        ...

    @abstractmethod 
    async def create_collection(self):
        ...

    @abstractmethod
    async def delete_collection(self):
        ...

    @abstractmethod
    async def collection_exists(self):
        ...


    @abstractmethod
    async def delete(self,ids):
        ...

    