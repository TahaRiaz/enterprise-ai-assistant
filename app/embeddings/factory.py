from app.embeddings.openai import OpenAIEmbeddingProvider


class EmbeddingProviderFactory:

    @staticmethod
    def create():
        return OpenAIEmbeddingProvider()
