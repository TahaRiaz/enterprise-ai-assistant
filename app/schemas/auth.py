from pydantic import BaseModel, ConfigDict, EmailStr, Field

class RegisterRequest(BaseModel):
    email: EmailStr
    username: str = Field(
        min_length=3,
        max_length= 50,
    )
    password: str = Field(
        min_length=8,
        max_length=120,
    )

class UserResponse(BaseModel):
    id:int
    email: EmailStr
    username: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class LoginRequest(BaseModel):
    email:EmailStr
    password:str

class TokenResponse(BaseModel):
    access_token: str
    token_type:str = "bearer"