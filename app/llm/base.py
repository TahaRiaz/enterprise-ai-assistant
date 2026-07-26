from abc import ABC,abstractmethod

class ChatModel(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt:str,
    ) -> str:
        ...

