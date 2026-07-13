from app.core.logger import app_logger

class BaseService:
    def __init__(self):
        self.logger = app_logger