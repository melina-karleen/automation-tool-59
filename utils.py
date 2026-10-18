from typing import Union, List
from decimal import Decimal

def format_crypto_amount(amount: Union[str, float, Decimal], precision: int = 8) -> str:
    """Format crypto currency values to fixed string representation."""
    return f"{Decimal(str(amount)):.{precision}f}"

def calculate_fee(amount: Decimal, rate: Decimal) -> Decimal:
    """Calculate transaction fees based on rate."""
    return (amount * rate).quantize(Decimal('0.00000001'))

def validate_ticker(ticker: str) -> bool:
    """Check if ticker format is valid."""
    if not ticker or not isinstance(ticker, str):
        return False
    return ticker.isupper() and 2 <= len(ticker) <= 10

def aggregate_balances(balances: List[dict]) -> dict:
    """Sum balances by asset type."""
    summary = {}
    for entry in balances:
        asset = entry['asset']
        amount = Decimal(str(entry['amount']))
        summary[asset] = summary.get(asset, Decimal('0')) + amount
    return {k: str(v) for k, v in summary.items()}