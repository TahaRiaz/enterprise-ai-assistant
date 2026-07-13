from fastapi import APIRouter,Depends
from app.schemas.health import HealthResponse
from app.services.health_service import HealthService
from app.dependencies.services import get_health_services

router = APIRouter()

@router.get("/health",response_model=HealthResponse, status_code=200,)
async def health_check(service: HealthService = Depends(get_health_services)):
    return service.get_health()
