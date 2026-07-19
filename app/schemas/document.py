from pydantic import (
    BaseModel, ConfigDict
)

class DocumentResponse(BaseModel):
    id:int
    filname:str
    original_filename:str
    status:str
    model_config = ConfigDict(
        from_attributes=True
    )