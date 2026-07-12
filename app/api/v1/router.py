from fastapi import APIRouter

from app.api.v1.endpoints import heath

router = APIRouter()

router.include_router(
    heath.router,
    tags=["Health"],
)