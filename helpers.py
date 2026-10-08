import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def validate_order_params(params: Dict[str, Any]) -> bool:
    required = {'symbol', 'side', 'quantity', 'price'}
    return all(key in params for key in required)

def retry_request(func, retries: int = 3, delay: int = 2):
    def wrapper(*args, **kwargs):
        last_exception = None
        for i in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                time.sleep(delay * (2 ** i))
        logger.error(f"failed after {retries} attempts: {last_exception}")
        raise last_exception
    return wrapper

def sanitize_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}

def get_timestamp_ms() -> int:
    return int(time.time() * 1000)