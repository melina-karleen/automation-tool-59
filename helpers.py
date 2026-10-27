import hashlib
import hmac
import time
from typing import Dict, Any
from urllib.parse import urlencode

def generate_signature(secret: str, message: str) -> str:
    return hmac.new(
        secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def build_query_string(params: Dict[str, Any]) -> str:
    return urlencode(sorted(params.items()))

def get_timestamp_ms() -> int:
    return int(time.time() * 1000)

def format_price(price: float, precision: int = 8) -> str:
    return f"{price:.{precision}f}".rstrip('0').rstrip('.')

def validate_order_params(params: Dict[str, Any]) -> bool:
    required = ['symbol', 'side', 'type', 'quantity']
    return all(key in params for key in required)

def calculate_fee(amount: float, rate: float) -> float:
    return round(amount * rate, 8)