from fastapi import Depends

from app.core.oauth2 import oauth2_scheme
from app.core.security import decode_access_token
from app.dependencies.repositories import (get_user_repository,)
from app.repositories.user import UserRepository
from app.core.exceptions import AppException

async def get_current_user(
        token:str = Depends(
            oauth2_scheme,
        ),
        repository: UserRepository = Depends(
            get_user_repository,
        ),
):
    payload = decode_access_token(token=token)

    user_id = int(payload['sub'])

    user = repository.get(user_id)

    if not user:
        raise AppException(
            "User not found."
        )
    
    if not user.is_active:
        raise AppException(
            "Inactive user"
        )
    return user

async def require_superuser(
        current_user = Depends(
            get_current_user,
        )
):
    if not current_user.is_superuser:
        raise AppException(
            "Access denied"
        )
    
    return current_user



