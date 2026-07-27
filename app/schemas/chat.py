
from pydantic import BaseModel,ConfigDict

class ChatResponse(BaseModel):

    answer:str

    model_config = ConfigDict(from_attributes=True)


class ChatRequest(BaseModel):
    question: str
    conversation_id: int | None = None
    user_id: int


    model_config = ConfigDict(from_attributes=True)