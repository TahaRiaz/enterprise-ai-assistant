from fastapi import APIRouter,Depends
from app.schemas.health import HealthResponse
from app.services.health_service import HealthService
from app.dependencies.services import get_health_services
from app.schemas.common import ApiResponse
from app.core.messages import SuccessMessage
from app.core.constants import APITags

router = APIRouter(
    prefix="/health",
    tags=[APITags.HEALTH]
)

@router.get("/",response_model=ApiResponse[HealthResponse], status_code=200,)
async def health_check(service: HealthService = Depends(get_health_services)):
    return ApiResponse(
        success=True,
        message=SuccessMessage.HEALTH_CHECK,
        data=service.get_health()
    )
