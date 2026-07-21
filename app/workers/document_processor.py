from app.database.models.document import Document
from app.parsers.factory import ParserFactory
from app.chunkers.recursive import RecursiveChunker
from app.embeddings.factory import EmbeddingProviderFactory


class DocumentProcessor:

    def __init__(self, document):
        self.document = document

    async def process_document(self, document:Document):
        
        """
        Process the document with the given document_id.
        """

        ## Step 1: Parse the document
        parser = ParserFactory.create(content_type=document.content_type)
        parsed_document = await parser.parse(document=document)

        ## Step 2: Chunk the document

        chunker = RecursiveChunker()
        chunks = chunker.chunk(document=parsed_document)

        ## Step 3: Genrate vector embeddings for each chunk
        embedding_provider = EmbeddingProviderFactory.create()
        vectors = await embedding_provider.embed(
            [
                chunk.text for chunk in chunks
            ]
        )




