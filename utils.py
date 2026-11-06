from decimal import Decimal, ROUND_DOWN
from typing import Tuple


def sats_to_btc(sats: int) -> Decimal:
    """Convert satoshis to a Bitcoin Decimal representation.

    Args:
        sats: Amount in satoshis.

    Returns:
        Decimal representation of the amount in BTC.
    """
    if sats < 0:
        raise ValueError("Satoshis must be a non-negative integer.")
    return Decimal(sats) / Decimal(100_000_000)


def calculate_slippage(expected_price: float, actual_price: float) -> float:
    """Calculate the percentage slippage between expected and actual price.

    Args:
        expected_price: Target trade execution price.
        actual_price: Realized trade execution price.

    Returns:
        Percentage difference as a float.
    """
    if expected_price <= 0:
        raise ValueError("Expected price must be greater than zero.")
    return abs(actual_price - expected_price) / expected_price * 100.0


def parse_trading_pair(pair: str) -> Tuple[str, str]:
    """Parse a symbol pair string into base and quote assets.

    Args:
        pair: Trading pair symbol (e.g., 'BTC/USDT' or 'ETH-USDC').

    Returns:
        Tuple containing (base_asset, quote_asset).
    """
    separator = "/" if "/" in pair else "-" if "-" in pair else ""
    if not separator:
        raise ValueError(f"Invalid trading pair format: {pair}")
    base, quote = pair.split(separator, 1)
    return base.upper().strip(), quote.upper().strip()


def truncate_precision(value: float, precision: int = 8) -> float:
    """Truncate a floating point value to a specified decimal precision.

    Args:
        value: Number to truncate.
        precision: Number of decimal places to retain.

    Returns:
        Truncated float value.
    """
    if precision < 0:
        raise ValueError("Precision cannot be negative.")
    quantum = Decimal("10") ** -precision
    return float(Decimal(str(value)).quantize(quantum, rounding=ROUND_DOWN))
