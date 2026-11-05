import re
from typing import Any
from exceptions import ValidationError

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_eth_address(address: str) -> bool:
    if not isinstance(address, str) or not ADDRESS_PATTERN.match(address):
        raise ValidationError(f'invalid ethereum address: {address}')
    return True

def validate_amount(amount: Any) -> float:
    try:
        val = float(amount)
        if val <= 0:
            raise ValueError
        return val
    except (ValueError, TypeError):
        raise ValidationError(f'invalid numeric amount: {amount}')

def validate_chain_id(chain_id: int) -> int:
    if not isinstance(chain_id, int) or chain_id <= 0:
        raise ValidationError(f'invalid chain identifier: {chain_id}')
    return chain_id

def validate_payload(data: dict, required_keys: list) -> None:
    for key in required_keys:
        if key not in data:
            raise ValidationError(f'missing required field: {key}')