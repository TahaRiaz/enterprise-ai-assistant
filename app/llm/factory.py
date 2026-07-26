from app.llm.openai import OpenAi

class LlmFactory:

    @staticmethod
    def get_llm():
        return OpenAi()