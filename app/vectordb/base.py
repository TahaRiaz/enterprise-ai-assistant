from abc import ABC, abstractmethod

class VectorStore(ABC):

    @abstractmethod
    async def upsert(self, vectors):
        ...

    @abstractmethod
    async def search(self, vector,limit:int):
        ...

    