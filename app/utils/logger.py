from loguru import logger
from app.config.settings import LOG_DIR

LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.add(
    LOG_DIR / "rag.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO"
)

__all__ = ["logger"]