import functools
import time
from typing import Callable, Any, Dict

CACHE: Dict[str, Any] = {}

def memoize_data(ttl: int = 60) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
            now = time.time()
            if key in CACHE:
                val, timestamp = CACHE[key]
                if now - timestamp < ttl:
                    return val
            result = func(*args, **kwargs)
            CACHE[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int = 100):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def clean_cache():
    CACHE.clear()