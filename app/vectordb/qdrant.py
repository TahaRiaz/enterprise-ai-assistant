from qdrant_client import AsyncQdrantClient
from app.config.settings import settings
from app.database.models.chunk import Chunk
from app.vectordb.base import VectorStore
from app.vectordb.schema import PointStruct


class QdrantVectorStore(VectorStore):


    def __init__(self):
        self.client = AsyncQdrantClient(url = settings.QDRANT_URL,)


    async def upsert(self, chunks: list[Chunk], vectors: list[list[float]], collection_name: str,user_id: int | None=None, ):

        points = []

        for chunk, vector in zip(chunks, vectors):
            payload = {
                "text": chunk.text,
                "document_id": chunk.document_id,
            }

            if user_id is not None:
                payload["user_id"] = user_id

            points.append(
                PointStruct(
                    id=chunk.id,
                    vector=vector,
                    payload=payload
                )
            )

        await self.client.upsert(
            collection_name=collection_name,
            points=points,
        )

    async def search(self, vector: list[float], limit: int, collection_name: str):
        await self.client.query_points(
            collection_name=collection_name,
            query=vector,
            limit=limit
        )

    async def create_collection(self, collection_name:str):
        await self.client.create_collection(
            collection_name=collection_name,
            vectors_config={
                "size": 1536,
                "distance": "Cosine"
            }
        )
    async def delete_collection(self, collection_name:str):
        await self.client.delete_collection(
            collection_name=collection_name
        )

    async def collection_exists(self, collection_name:str) -> bool:
        collections = await self.client.get_collections()
        return any(collection.name == collection_name for collection in collections.collections)