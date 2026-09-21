from typing import Final, Dict, List

EXCHANGE_IDS: Final[List[str]] = ['binance', 'coinbase', 'kraken']
API_TIMEOUT: Final[int] = 30
RETRY_ATTEMPTS: Final[int] = 3

PRECISION_MAP: Final[Dict[str, int]] = {
    'BTC': 8,
    'ETH': 6,
    'USDT': 2
}

DATABASE_URI: Final[str] = 'postgresql://localhost:5432/automation'
MIN_TRADE_VOLUME: Final[float] = 0.001


def get_precision(symbol: str) -> int:
    """Return decimal precision for given crypto asset."""
    return PRECISION_MAP.get(symbol, 4)


def is_supported_exchange(exchange: str) -> bool:
    """Validate if the exchange exists in whitelist."""
    return exchange in EXCHANGE_IDS
