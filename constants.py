"""Crypto automation tool constants and configuration defaults."""

from enum import Enum
from typing import Dict, Final, List


class NetworkEnv(str, Enum):
    """Supported blockchain network environments."""

    MAINNET = "mainnet"
    TESTNET = "testnet"
    DEVNET = "devnet"


class ExchangeID(str, Enum):
    """Supported cryptocurrency exchanges."""

    BINANCE = "binance"
    BYBIT = "bybit"
    KRAKEN = "kraken"


DEFAULT_TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 5
DEFAULT_SLIPPAGE_TOLERANCE: Final[float] = 0.005

PRECISION_MAP: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6,
    "USDC": 6,
    "SOL": 9,
}

SUPPORTED_PAIRS: Final[List[str]] = [
    "BTC/USDT",
    "ETH/USDT",
    "SOL/USDT",
    "BTC/USDC",
    "ETH/USDC",
]

DEFAULT_GAS_LIMITS: Final[Dict[str, int]] = {
    "transfer": 21000,
    "token_transfer": 65000,
    "swap": 250000,
}
