from typing import Any, Optional

class ValidationError(Exception):
    pass

def validate_wallet_address(address: Any) -> str:
    if not isinstance(address, str):
        raise ValidationError('address must be a string')
    if len(address) != 42 or not address.startswith('0x'):
        raise ValidationError('invalid ethereum address format')
    return address

def validate_amount(amount: Any) -> float:
    try:
        value = float(amount)
    except (ValueError, TypeError):
        raise ValidationError('amount must be a numeric value')
    if value <= 0:
        raise ValidationError('amount must be greater than zero')
    return value

def validate_network_payload(payload: Optional[dict]) -> dict:
    if not payload or not isinstance(payload, dict):
        raise ValidationError('payload must be a non-empty dictionary')
    required_keys = {'tx_hash', 'gas_price'}
    if not required_keys.issubset(payload.keys()):
        missing = required_keys - payload.keys()
        raise ValidationError(f'missing required fields: {missing}')
    return payload