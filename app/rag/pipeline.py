from app.core.exceptions import AppException

class RAGPipeline:

    def __init__(
            self,
            retriever,
            prompt_builder,
            llm,
    ):

        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm


    async def ask(
            self,
            question:str,
    ):

        chunks = self.retriever.retrieve(
            question
        )

        if not chunks:
            return AppException(
                "I counld not find relevant information in your documents."
            )

        prompt = self.prompt_builder.build(
            question,
            chunks,
        )

        answer = await self.llm.generate(
            prompt
        )

        return answer


    async def strea(
            self,
            question:str,
    ):

        chunks = self.retriever.retrieve(
            question
        )

        if not chunks:
            return AppException(
                "I counld not find relevant information in your documents."
            )

        prompt = self.prompt_builder.build(
            question,
            chunks,
        )

        return self.llm.stream(prompt)