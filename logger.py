import logging
import sys
from typing import Optional

class CryptoLogger:
    """Custom logger for automation-tool-59 operations."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg: str, *args: object) -> None:
        """Log informational messages."""
        self.logger.info(msg, *args)

    def error(self, msg: str, exc_info: Optional[bool] = None) -> None:
        """Log error messages with optional traceback."""
        self.logger.error(msg, exc_info=exc_info)

def get_logger(name: str) -> logging.Logger:
    """Factory function to retrieve named logger instance."""
    return CryptoLogger(name).logger