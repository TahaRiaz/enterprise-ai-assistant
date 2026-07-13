from fastapi import APIRouter,Depends
from app.schemas.health import HealthResponse
from app.services.health_service import HealthService
from app.dependencies.services import get_health_services
from app.schemas.common import ApiResponse

router = APIRouter()

@router.get("/health",response_model=ApiResponse[HealthResponse], status_code=200,)
async def health_check(service: HealthService = Depends(get_health_services)):
    return ApiResponse(
        success=True,
        message="Health check completed successfully.",
        data=service.get_health()
    )
