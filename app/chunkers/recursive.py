from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from app.chunkers.schema import TextChunk
from app.chunkers.base import TextChunker

class RecursiveChunker(TextChunker):

    def __init__(
            self,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )

    def chunk(
            self, document,
    ):
        chunks = []

        index = 0

        for page in document.pages:

            texts = self.splitter.split_text(page.text)

            for count,text in enumerate(texts):
                index = count +1
                chunks.append(
                    TextChunk(
                        text=text,
                        page_number=page.page_number,
                        chunk_index = index,
                    )
                )

        return chunks
    

