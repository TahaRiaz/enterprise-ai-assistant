from pwdlib import PasswordHash

passwordHash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return passwordHash.hash(password=password)


def verify_password(plain_password: str, hash_password: str) -> bool:
    return passwordHash.verify(password=plain_password, hash=hash_password,)