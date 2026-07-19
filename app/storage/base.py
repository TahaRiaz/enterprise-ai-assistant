from abc import ABC
from abc import abstractmethod

class StrorageProvider(ABC):
    
    @abstractmethod
    async def save(
        self,
        filename:str,
        content: bytes,
    ) -> str:
        """
        Returns storage path.
        """