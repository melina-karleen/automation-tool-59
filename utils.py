import json
from decimal import Decimal
from typing import Any, Dict

def normalize_crypto_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Sanitizes and converts crypto pricing data."""
    normalized = {}
    for key, value in data.items():
        if isinstance(value, (str, float, int)):
            try:
                normalized[key] = float(Decimal(str(value)))
            except Exception:
                normalized[key] = value
        else:
            normalized[key] = value
    return normalized

def validate_ticker(ticker: str) -> bool:
    """Checks format of trading pairs."""
    return isinstance(ticker, str) and '/' in ticker and len(ticker) <= 12

def format_order_payload(symbol: str, side: str, amount: float) -> str:
    """Serializes order request to JSON string."""
    payload = {
        "symbol": symbol.upper(),
        "side": side.lower(),
        "amount": float(amount)
    }
    return json.dumps(payload)