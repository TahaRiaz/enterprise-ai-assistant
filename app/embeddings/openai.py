from openai import AsyncOpenAI

from app.config.settings import settings
from app.embeddings.base import EmbeddingProvider

class OpenAIEmbeddingProvider(EmbeddingProvider):


    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )


    async def embed(
            self,
            texts: list[str],
    ) -> list[list[float]]: ## Vectors are list of float values here we are returning a
        ## a vectors for each chunk of text provided in the input
        
        response = await self.client.embeddings.create(
            model=settings.EMBEDDING_MODEL,
            input=texts
        )

        return [item.embedding for item in response.data]