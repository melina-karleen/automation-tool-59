class ValidationError(Exception):
    pass

def validate_trade_params(data: dict) -> None:
    required = {'symbol', 'amount', 'side'}
    if not all(key in data for key in required):
        raise ValidationError('missing required trade fields')
    
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        raise ValidationError('invalid trade amount')
    
    if data['side'] not in {'buy', 'sell'}:
        raise ValidationError('invalid trade side')

def validate_api_key(api_key: str) -> None:
    if not isinstance(api_key, str) or len(api_key) < 32:
        raise ValidationError('malformed api key detected')

if __name__ == '__main__':
    try:
        test_data = {'symbol': 'BTC', 'amount': 0.01, 'side': 'buy'}
        validate_trade_params(test_data)
    except ValidationError as e:
        print(f'validation error: {e}')