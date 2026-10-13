import re

class InputValidator:
    @staticmethod
    def validate_ticker(ticker: str) -> bool:
        return bool(re.match(r'^[A-Z0-9]{2,10}$', ticker))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def validate_price(price: float) -> bool:
        return isinstance(price, (int, float)) and price >= 0

def process_input(data: dict):
    ticker = data.get('ticker', '')
    amount = data.get('amount', 0)
    price = data.get('price', 0)

    if not InputValidator.validate_ticker(ticker):
        raise ValueError(f'Invalid ticker format: {ticker}')
    
    if not InputValidator.validate_amount(amount):
        raise ValueError(f'Invalid amount: {amount}')

    if not InputValidator.validate_price(price):
        raise ValueError(f'Invalid price: {price}')

    return True