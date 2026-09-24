from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Optional


def calculate_position_size(balance: str, risk_pct: float, entry: str, sl: str) -> Decimal:
    balance_dec = Decimal(balance)
    entry_dec = Decimal(entry)
    sl_dec = Decimal(sl)
    risk_amount = balance_dec * Decimal(str(risk_pct))
    price_diff = abs(entry_dec - sl_dec)
    if price_diff == 0:
        return Decimal('0')
    size = risk_amount / price_diff
    return size.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)


def normalize_ohlcv(data: Dict) -> Dict:
    return {
        'timestamp': int(data['t']),
        'open': float(data['o']),
        'high': float(data['h']),
        'low': float(data['l']),
        'close': float(data['c']),
        'volume': float(data['v'])
    }


def validate_ticker(ticker: str) -> bool:
    if not isinstance(ticker, str) or len(ticker) < 3:
        return False
    return ticker.replace('/', '').isalnum()