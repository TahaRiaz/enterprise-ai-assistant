from pwdlib import PasswordHash
from datetime import datetime,timedelta,timezone
from app.config.settings import settings
import jwt

passwordHash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return passwordHash.hash(password=password)


def verify_password(plain_password: str, hash_password: str) -> bool:
    return passwordHash.verify(password=plain_password, hash=hash_password,)

def create_access_token(user_id:int, email:str) ->str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub":str(user_id),
        "email": email,
        "exp":expire
    }

    return jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

def verify_access_token(token:str):
    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM],
    )