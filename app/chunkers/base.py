from abc import ABC, abstractmethod

from app.chunkers.schema import TextChunk
from app.parsers.schema import ParsedDocument


class TextChunker(ABC):


    @abstractmethod
    def chunk(
        self,
        document: ParsedDocument,
    ) -> list[TextChunk]:
        ...
