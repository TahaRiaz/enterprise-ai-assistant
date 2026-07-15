from loguru import logger
from pathlib import Path
import sys

#project root
BASE_DIR = Path(__file__).resolve().parents[2]

#Logs directory
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

#Remove default logger
logger.remove()

#console logging
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
)

#file logging
logger.add(
    LOG_DIR / "app.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
    enqueue=True,
    compression=zip
)

app_logger = logger