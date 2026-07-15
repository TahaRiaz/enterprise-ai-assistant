from app.core.exceptions import AppException
from app.core.security import hash_password
from app.database.models.user import User
from app.repositories.user import UserRepository
from app.schemas.auth import RegisterRequest

class AuthService:

    def __init__(
            self,
            user_repository: UserRepository
    ):
        self.user_repository = user_repository
        
    def register(
            self,
            request: RegisterRequest
    ):
        existing_user = (
            self.user_repository.get_by_email_or_username(
                email=request.email,
                username=request.username,
            )
        )

        if existing_user:
            raise AppException(
                "Email or Username already in use."
            )
        
        user = User(
            email = request.email,
            username = request.username,
            hash_password = hash_password(
                password=request.password,
            )
        )

        return self.user_repository.create(user)