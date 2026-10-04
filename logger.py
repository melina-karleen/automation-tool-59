import logging
import sys
from typing import Optional

class CryptoLogger:
    def __init__(self, name: str = "automation-tool-59"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, error: Exception, context: Optional[str] = None) -> None:
        error_msg = f"Context: {context} | " if context else ""
        self.logger.error(f"{error_msg}Exception: {type(error).__name__} - {str(error)}")

    def safe_execute(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError as e:
            self.log_error(e, "network failure")
        except ValueError as e:
            self.log_error(e, "invalid data input")
        except Exception as e:
            self.log_error(e, "unexpected critical failure")
        return None

logger = CryptoLogger()