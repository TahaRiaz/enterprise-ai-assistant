from app.repositories.chunk import ChunkRepository
from app.services.base_service import BaseService
from app.chunkers.schema import TextChunk
from app.database.models.chunk import Chunk



class ChunkService(BaseService):

    def __init__(self, chunk_repository: ChunkRepository):
        self.chunk_repository = chunk_repository



    def save_chunks(self, chunks:list[TextChunk], document_id: int):
        """
        Save the chunks to the database.
        """

        db_chunks = []

        for chunk in chunks:
            db_chunks.append(
                Chunk(
                    text=chunk.text,
                    page_number=chunk.page_number,
                    chunk_index=chunk.chunk_index,
                    document_id=document_id
                )
            )   
        return self.chunk_repository.create_many(db_chunks)
        