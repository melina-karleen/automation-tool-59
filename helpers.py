import time
import hashlib
import hmac
from typing import Dict, Any
from decimal import Decimal

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_amount(amount: float, precision: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(f"1.{'0' * precision}"))

def get_timestamp_ms() -> int:
    return int(time.time() * 1000)

def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in payload.items() if v is not None}

def calculate_fee(amount: float, rate: float) -> Decimal:
    return Decimal(str(amount)) * Decimal(str(rate))