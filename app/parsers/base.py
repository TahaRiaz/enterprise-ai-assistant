from abc import ABC, abstractmethod


from app.parsers.schema import ParsedDocument

class DocumentParser(ABC):

    def __init__(self, ):
        pass

    @abstractmethod
    def parse(
        self,
        file_path: str,
    ) -> ParsedDocument:
        
        """
        Pass the document in the given format
        """
