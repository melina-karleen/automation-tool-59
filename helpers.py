import time
import functools
from typing import Callable, Any

def retry(retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def validate_address(address: str, length: int = 42) -> bool:
    return isinstance(address, str) and len(address) == length and address.startswith('0x')

def calculate_fee(amount: float, rate: float) -> float:
    return max(0.0, amount * rate)