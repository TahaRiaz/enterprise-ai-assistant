from dataclasses import dataclass

@dataclass
class RetrievedChunk:
    """
    Represents a chunk of text retrieved from a document, along with its metadata.
    
    """

    text:str
    score: float
    document_id: str
    page_number:int
    chunk_index: int
    