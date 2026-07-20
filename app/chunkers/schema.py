from dataclasses import dataclass

@dataclass
class TextChunk:
    text: str
    page_number: int
    chunk_index: int

    