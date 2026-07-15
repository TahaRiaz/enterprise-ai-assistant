from app.services.health_service import HealthService
from app.dependencies.repositories import get_user_repository
from app.repositories.user import UserRepository
from app.services.auth_service import AuthService
from fastapi import Depends

def get_health_services() -> HealthService:
    return HealthService()

def get_auth_service(repository: UserRepository = Depends(get_user_repository,)):
    return AuthService(repository)