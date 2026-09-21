import re
from decimal import Decimal, InvalidOperation
from typing import Any

class ValidationError(Exception):
    pass

def validate_asset_symbol(symbol: Any) -> str:
    if not isinstance(symbol, str) or not re.fullmatch(r'[A-Z0-9]{2,10}', symbol):
        raise ValidationError(f"Invalid asset symbol: {symbol}")
    return symbol

def validate_amount(amount: Any) -> Decimal:
    try:
        value = Decimal(str(amount))
        if value <= 0:
            raise ValidationError(f"Amount must be positive: {amount}")
        return value
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValidationError(f"Invalid amount format: {amount}") from e

def validate_chain_id(chain_id: Any) -> int:
    try:
        value = int(chain_id)
        if value < 1:
            raise ValidationError(f"Chain ID must be positive: {chain_id}")
        return value
    except (ValueError, TypeError) as e:
        raise ValidationError(f"Invalid chain ID format: {chain_id}") from e

def validate_transaction_payload(data: dict) -> dict:
    required_fields = ['symbol', 'amount', 'chain_id']
    if not all(field in data for field in required_fields):
        raise ValidationError("Missing required transaction fields")
    
    return {
        'symbol': validate_asset_symbol(data['symbol']),
        'amount': validate_amount(data['amount']),
        'chain_id': validate_chain_id(data['chain_id'])
    }