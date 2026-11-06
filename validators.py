import re

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_crypto_address(address: str) -> bool:
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def validate_symbol(symbol: str) -> bool:
    return isinstance(symbol, str) and 2 <= len(symbol) <= 10

def validate_payload(data: dict) -> bool:
    required = ['address', 'amount', 'symbol']
    if not all(key in data for key in required):
        return False
    return (
        validate_crypto_address(data['address']) and
        validate_amount(data['amount']) and
        validate_symbol(data['symbol'])
    )