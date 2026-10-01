from typing import Any, Dict, Optional
import re

def validate_ticker(ticker: str) -> bool:
    return bool(re.match(r'^[A-Z0-9]{2,10}$', ticker))

def validate_price(price: Any) -> bool:
    try:
        return float(price) > 0
    except (ValueError, TypeError):
        return False

def validate_payload(data: Dict[str, Any]) -> bool:
    required = ['ticker', 'price', 'volume']
    if not all(k in data for k in required):
        return False
    return validate_ticker(data['ticker']) and validate_price(data['price'])

def sanitize_currency(symbol: str) -> str:
    return symbol.strip().upper().replace('/', '_')

def format_precision(value: float, decimals: int = 8) -> float:
    return round(float(value), decimals)