from app.schemas.health import HealthResponse
from app.config.settings import settings
from app.services.base_service import BaseService

class HealthService(BaseService):

    def get_health(self) -> HealthResponse:
        self.logger.info("Health check requested.")
        return HealthResponse(
            status="healty",
            application= settings.APP_NAME,
            version=settings.APP_VERSION
        )