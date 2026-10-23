import logging
import sys
from typing import Any

class CryptoLogger:
    def __init__(self, name: str = "automation-tool-59") -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, operation: str, error: Exception) -> None:
        error_type = type(error).__name__
        self.logger.error(f"failed {operation}: {error_type} - {str(error)}")

    def safe_execute(self, operation: str, func: Any, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except ConnectionError as e:
            self.log_error(f"{operation} (network failure)", e)
        except ValueError as e:
            self.log_error(f"{operation} (validation failure)", e)
        except Exception as e:
            self.log_error(f"{operation} (unexpected critical error)", e)
        return None

logger = CryptoLogger()