import re


def validate_trade_params(data: dict) -> bool:
    required_fields = {'symbol', 'side', 'amount', 'price'}
    if not all(k in data for k in required_fields):
        return False
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return False
    if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return False
    if not re.match(r'^[A-Z]{3,10}/[A-Z]{3,10}$', data['symbol']):
        return False
    return data['side'] in {'buy', 'sell'}


def validate_api_key(api_key: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9]{32,64}$', api_key))