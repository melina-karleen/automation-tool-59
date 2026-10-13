import logging
import sys
from typing import Optional

class CryptoLogger:
    """Custom logger for automation-tool-59 operations."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message: str) -> None:
        """Log informational messages to stdout."""
        self.logger.info(message)

    def log_error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log error messages with optional exception info."""
        self.logger.error(message, exc_info=exc_info)

    def log_warning(self, message: str) -> None:
        """Log warning level messages."""
        self.logger.warning(message)