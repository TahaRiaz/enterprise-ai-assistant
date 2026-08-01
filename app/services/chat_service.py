from app.core.exceptions import AppException
from app.database.models.message import Message
from app.schemas.chat import ChatRequest,ChatMessage

class ChatService:

    def __init__(
            self,
            conversation_repository,
            message_repository,
            pipeline,
    ):
        self.conversation_repo = conversation_repository
        self.message_repo = message_repository,
        self.pipeline = pipeline


    async def chat(
            self,
            converastion_id: int | None,
            question: str,
            current_user,
    ):

        if converastion_id is None:
            conversation = await self.conversation_repo.create_conversation(
                ChatRequest(
                    question=question,
                    conversation_id=converastion_id,
                    user_id=current_user.id
                )
            )
        else:
            conversation = await self.conversation_repo.get_by_id_and_user(
                        converastion_id,
                        current_user.id,
                    )

        if conversation is None:
            raise AppException("Conversation not found.")

        message = Message(
            role = "user",
            content= question,
            converastion_id = converastion_id
        )
        await self.message_repo.add_message(
            message
        )

        messages = await self.message_repo.get_recent_messages(
            conversation.id,
        )

        history = [
            ChatMessage(
                role=message.role,
                content = message.content,
            )
            for message in messages
        ]

        answer = await self.pipeline.stream(
            question,
            history
        )

        await self.message_repo.add_message(
            Message(
                role="assistant",
                converastion_id=converastion_id,
                content=answer,
            )
        )
        return answer