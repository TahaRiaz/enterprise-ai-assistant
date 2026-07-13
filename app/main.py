from fastapi import FastAPI

from app.api.router import api_router
from app.config.settings import settings

from app.core.exceptions import AppException
from app.core.exception_handlers import app_exception_handler

from app.core.logger import app_logger
from contextlib import asynccontextmanager

from app.middleware.request_logger import RequestLoggingMiddleware
@asynccontextmanager
async def lifespan(app:FastAPI):
    app_logger.info("Application starting....")
    yield
    app_logger.info("Application shutting down....")


app = FastAPI(
    title= settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

app.add_exception_handler(
    AppException,
    app_exception_handler,
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(api_router)