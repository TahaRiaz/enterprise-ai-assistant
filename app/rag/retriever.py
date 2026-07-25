

class Retiever:

    def __init__(self, embedder,vector_store,):
        self.embedder = embedder
        self.vector_store = vector_store


    async def retrieve(self, question, limit: int = 5,):

        """
        Retrieves relevant chunks of text based on the provided question.

        Args:
            question (str): The question or query to retrieve relevant chunks for.
            limit (int): The maximum number of chunks to retrieve. Default is 5.

        Returns:
            List[RetrievedChunk]: A list of RetrievedChunk objects containing the retrieved text and metadata.
        """

        embedding = await self.embedder.embed([question])

        results = await self.vector_store.search(embedding[0], limit = limit)

        return results


        # # Embed the question using the embedder
        # question_embedding = self.embedder.embed(question)

        # # Query the vector store for relevant chunks
        # retrieved_chunks = await self.vector_store.query(question_embedding, limit=limit)

        # return retrieved_chunks