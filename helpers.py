import time
import logging
from typing import Any, Callable, Dict

logger = logging.getLogger(__name__)

def retry_operation(func: Callable, retries: int = 3, delay: int = 2) -> Any:
    last_exception = None
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            logger.warning(f"attempt {i+1} failed: {e}")
            time.sleep(delay)
    raise last_exception

def format_crypto_amount(value: float, precision: int = 8) -> str:
    return f"{value:.{precision}f}"

def sanitize_config(config: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in config.items() if v is not None}

def validate_connection(status_code: int) -> bool:
    return 200 <= status_code < 300