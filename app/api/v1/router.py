from fastapi import APIRouter

from app.api.v1.endpoints import health
from app.api.v1.endpoints import auth
from app.core.constants import APITags

router = APIRouter()

router.include_router(
    health.router,
    tags=[APITags.HEALTH],
)

router.include_router(
    auth.router,
    tags=[APITags.AUTH]

)