import time
import logging
from typing import Callable, Any
from decimal import Decimal, ROUND_HALF_UP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("automation-tool-59")

def retry_operation(retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            last_ex = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    time.sleep(delay * (2 ** i))
            raise last_ex
        return wrapper
    return decorator

def format_crypto(value: float, precision: int = 8) -> Decimal:
    return Decimal(str(value)).quantize(
        Decimal(10) ** -precision, 
        rounding=ROUND_HALF_UP
    )

def validate_order_size(amount: float, min_size: float) -> bool:
    return amount >= min_size

def get_timestamp() -> int:
    return int(time.time() * 1000)