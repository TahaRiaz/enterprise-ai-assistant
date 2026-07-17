from fastapi import APIRouter
from fastapi import Depends
from app.schemas.auth import UserResponse

from app.dependencies.auth import (
    get_current_user,
    require_superuser
)

from app.database.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me")
async def me(
    current_user: User = Depends(
        get_current_user,
    ),
):
    return UserResponse.model_validate(current_user)

# @router.delete("/{id}")
# async def delete_user(
#     current_user: User = Depends(
#         require_superuser,
#     )
# ):
#     if 