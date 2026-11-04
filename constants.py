from typing import Final
from enum import Enum

class ExchangeLimits(Enum):
    MAX_RETRIES: int = 3
    TIMEOUT_SEC: float = 0.5
    BUFFER_SIZE: int = 1024

CACHE_TTL_SECONDS: Final[int] = 300
PRECISION_DIGITS: Final[int] = 8

DEFAULT_HEADERS: Final[dict[str, str]] = {
    "Content-Type": "application/json",
    "User-Agent": "automation-tool-59/1.0"
}

RATE_LIMIT_BUCKET_SIZE: Final[int] = 50
BATCH_PROCESS_THRESHOLD: Final[int] = 100

VALID_ASSETS: Final[set[str]] = {"BTC", "ETH", "SOL", "ADA", "DOT"}

def get_timeout() -> float:
    return ExchangeLimits.TIMEOUT_SEC.value

def get_batch_size() -> int:
    return BATCH_PROCESS_THRESHOLD