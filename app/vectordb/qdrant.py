from qdrant_client import AsyncQdrantClient
from app.config.settings import settings
from app.vectordb.base import VectorStore


class QdrantVectorStore(VectorStore):


    def __init__(self):
        self.client = AsyncQdrantClient(url = settings.QDRANT_URL,)


    async def upsert(self, vectors,collection_name: str):

        await self.client.upsert(
            collection_name=collection_name,
            points=vectors
        )

    async def search(self, vector, limit, collection_name:str):
        await self.client.query_points(
            collection_name=collection_name,
            query=vector,
            limit=limit
        )