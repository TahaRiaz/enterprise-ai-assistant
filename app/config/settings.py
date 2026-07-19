from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION:str
    DEBUG: bool
    ENTPRISE_API_V1_PREFIX: str
    DATABASE_URL: str
    JWT_SECRET_KEY:str
    JWT_ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    MAX_FILE_SIZE:int
    ALLOWED_DOCUMENT_EXTENSIONS: dict
    ALLOWED_TYPES:dict



    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()