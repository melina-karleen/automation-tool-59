from enum import Enum
from typing import Final


class CryptoChain(str, Enum):
    ETHEREUM = "ethereum"
    SOLANA = "solana"
    BINANCE = "bsc"
    ARBITRUM = "arbitrum"
    OPTIMISM = "optimism"


class OrderType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"
    STOP_LOSS = "stop_loss"
    TAKE_PROFIT = "take_profit"


class TradeStatus(str, Enum):
    PENDING = "pending"
    EXECUTED = "executed"
    FAILED = "failed"
    CANCELLED = "cancelled"


DEFAULT_SLIPPAGE_BPS: Final[int] = 50
MAX_SLIPPAGE_BPS: Final[int] = 1000
DEFAULT_GAS_LIMIT: Final[int] = 300000
DEFAULT_TIMEOUT_SECONDS: Final[int] = 30
STABLECOIN_SYMBOLS: Final[set[str]] = {"USDT", "USDC", "DAI", "BUSD", "FDUSD"}
PRECISION_DECIMALS: Final[dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "SOL": 9,
    "USDT": 6,
    "USDC": 6,
}
