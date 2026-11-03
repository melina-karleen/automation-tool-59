from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Optional

class CryptoDataHandler:
    def __init__(self, precision: int = 8):
        self.precision = precision

    def format_price(self, price: str) -> Decimal:
        return Decimal(price).quantize(Decimal(f"1.{'0' * self.precision}"), rounding=ROUND_HALF_UP)

    def calculate_position_size(self, balance: float, risk_per_trade: float) -> Decimal:
        return Decimal(str(balance * risk_per_trade)).quantize(Decimal('0.0001'))

    def parse_market_data(self, data: Dict) -> Optional[Dict]:
        try:
            return {
                "symbol": data["s"],
                "price": self.format_price(data["p"]),
                "volume": Decimal(data["q"]),
                "timestamp": int(data["t"])
            }
        except (KeyError, ValueError, TypeError):
            return None

    def validate_ticker(self, ticker: str) -> bool:
        return bool(ticker and isinstance(ticker, str) and "/" in ticker)

def sanitize_order_book(data: list) -> list:
    return sorted([{
        "price": Decimal(item[0]),
        "amount": Decimal(item[1])
    } for item in data], key=lambda x: x["price"])
