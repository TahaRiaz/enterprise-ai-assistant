from qdrant_client import AsyncQdrantClient
from app.config.settings import settings
from app.vectordb.base import VectorStore


class QdrantVectorStore(VectorStore):


    def __init__(self):
        self.client = AsyncQdrantClient(url = settings.QDRANT_URL,)

    