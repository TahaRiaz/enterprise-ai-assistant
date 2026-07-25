

class PromptBuilder:

    SYSTEM_PROMPT = """
You are an AI Assistant for an enterprise. Your role is to provide short and concise answers.

Answer ONLY using the provided context"""

    def build(
            self,
            question: str,
            chunks,
    ) -> str:

        context = "\n\n".join(
            f"[Page ${c.page_number}]\n${c.text}"
            for c in chunks
        )

        return f"""
{self.SYSTEM_PROMPT}

Context:

{context}

Question:

{question}

Answer:
"""