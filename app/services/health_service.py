from app.schemas.health import HealthResponse
from app.config.settings import settings

class HealthService:

    def get_health(self) -> HealthResponse:
        return HealthResponse(
            status="healty",
            application= settings.APP_NAME,
            version=settings.APP_VERSION
        )