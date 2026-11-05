from typing import Final
from enum import Enum

CACHE_TTL_SECONDS: Final[int] = 300
MAX_RETRIES: Final[int] = 3
DEFAULT_TIMEOUT: Final[float] = 10.5
BATCH_SIZE: Final[int] = 100

class ExchangeType(Enum):
    BINANCE = 'binance'
    COINBASE = 'coinbase'
    KRAKEN = 'kraken'

API_ENDPOINTS: Final[dict[ExchangeType, str]] = {
    ExchangeType.BINANCE: 'https://api.binance.com',
    ExchangeType.COINBASE: 'https://api.exchange.coinbase.com',
    ExchangeType.KRAKEN: 'https://api.kraken.com'
}

SUPPORTED_PAIRS: Final[tuple[str, ...]] = (
    'BTC-USD',
    'ETH-USD',
    'SOL-USD',
    'ADA-USD'
)

RATE_LIMIT_DELAY: Final[float] = 0.05
MEMORY_THRESHOLD_MB: Final[int] = 1024