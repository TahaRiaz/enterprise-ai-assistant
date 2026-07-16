from fastapi import APIRouter, Depends, status

from app.dependencies.services import get_auth_service
from app.schemas.auth import (
    RegisterRequest,
    UserResponse,
    TokenResponse,
    LoginRequest
)
from app.schemas.common import ApiResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/regiter", status_code=status.HTTP_201_CREATED,response_model=ApiResponse[UserResponse],)
async def register(
    request: RegisterRequest,
    service: AuthService = Depends(
        get_auth_service
    ),
):
    user = service.register(request=request)
    
    return ApiResponse(
        success=True,
        message="User registered successfully.",
        data=UserResponse.model_validate(user),
    )

@router.post("/login", response_model=ApiResponse[TokenResponse])
async def login(
    request: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    token = service.login(request=request)

    return ApiResponse(
        success=True,
        message="Login successful.",
        data=token,
    )

