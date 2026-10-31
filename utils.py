from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any


def format_crypto_amount(amount: float | str | Decimal, precision: int = 8) -> str:
    d = Decimal(str(amount))
    fmt = f"0.{'0' * precision}"
    return str(d.quantize(Decimal(fmt), rounding=ROUND_HALF_UP))


def normalize_symbol(symbol: str) -> str:
    clean = symbol.upper().replace("-", "").replace("_", "").replace("/", "")
    for quote in ["USDT", "USDC", "BUSD", "BTC", "ETH"]:
        if clean.endswith(quote) and len(clean) > len(quote):
            base = clean[:-len(quote)]
            return f"{base}/{quote}"
    return symbol.upper()


def calculate_price_change(entry_price: float, current_price: float) -> float:
    if entry_price <= 0:
        raise ValueError("Entry price must be greater than zero")
    return ((current_price - entry_price) / entry_price) * 100.0


def parse_ticker(data: Dict[str, Any]) -> Dict[str, Any]:
    symbol = normalize_symbol(str(data.get("symbol", "")))
    last_price = float(data.get("lastPrice", data.get("close", 0.0)))
    volume = float(data.get("volume", data.get("baseVolume", 0.0)))
    return {
        "symbol": symbol,
        "last_price": last_price,
        "volume": volume,
        "timestamp": data.get("timestamp") or data.get("time"),
    }
