from app.vectordb.qdrant import QdrantVectorStore

class VectorStoreFactory:

    @staticmethod
    def get_vector_store():
        return QdrantVectorStore()