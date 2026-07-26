from openai import AsyncOpenAI
from app.llm.base import ChatModel
from app.config.settings import settings

class OpenAi(ChatModel):

    def __init__(
            self,
    ):
        self.client = AsyncOpenAI(
            api_key= settings.OPENAI_API_KEY
        )


    async def generate(
            self,
            prompt:str
    ) -> str:
        response = await self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt
        )

        return response.output_text