from app.schemas.chat import ChatMessage

class PromptBuilder:

    SYSTEM_PROMPT = """
You are an AI Assistant for an enterprise. Your role is to provide short and concise answers.

Answer ONLY using the provided context"""

    def build(
            self,
            question: str,
            history,
            chunks,
          
    ) -> str:

        history_text = self._format_history(history=history)

        context = "\n\n".join(
            f"[Page ${c.page_number}]\n${c.text}"
            for c in chunks
        )

        return f"""
{self.SYSTEM_PROMPT}


History:
{history_text}

Context:
{context}

Question:
{question}

Answer:
"""

    def _format_history(
            self,
            history: list[ChatMessage],
    ) -> str:
        if not history:
            return ""

        lines = []

        for message in history:
            lines.append(
                f"{message.role.title()}: {message.content}"
            )

        return "\n".join(lines)