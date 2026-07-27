from abc import ABC,abstractmethod
from collections.abc import AsyncIterator

class ChatModel(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt:str,
    ) -> str:
        ...


    @abstractmethod
    async def stream(
        self,
        prompt:str,
    ) -> AsyncIterator[str]:
        ...    

