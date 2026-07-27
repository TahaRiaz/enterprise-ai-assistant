from openai import AsyncOpenAI
from app.llm.base import ChatModel
from app.config.settings import settings
from collections.abc import AsyncIterator
from app.core.exceptions import AppException

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


    async def generate(
            self,
            prompt:str
    )-> AsyncIterator[str,None]:
        stream = await self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt,
            stream=True,
        )

        async for event in stream:
            if event.type == "response.output_text.delta":
                yield event.delta

            elif event.type == "response.completed":
                break

            elif event.type == "response.error":
                raise AppException(event.error)