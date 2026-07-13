from app.services.health_service import HealthService

def get_health_services() -> HealthService:
    return HealthService()