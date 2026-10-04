import asyncio
import functools
import logging
import time
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger("automation_tool.utils")


def retry(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = Exception,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        if asyncio.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
                current_delay = delay
                for attempt in range(retries + 1):
                    try:
                        return await func(*args, **kwargs)
                    except exceptions as e:
                        if attempt == retries:
                            logger.error(f"Failed after {retries} retries: {e}")
                            raise
                        logger.warning(f"Retrying in {current_delay}s: {e}")
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff

            return async_wrapper
        else:

            @functools.wraps(func)
            def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
                current_delay = delay
                for attempt in range(retries + 1):
                    try:
                        return func(*args, **kwargs)
                    except exceptions as e:
                        if attempt == retries:
                            logger.error(f"Failed after {retries} retries: {e}")
                            raise
                        logger.warning(f"Retrying in {current_delay}s: {e}")
                        time.sleep(current_delay)
                        current_delay *= backoff

            return sync_wrapper

    return decorator
