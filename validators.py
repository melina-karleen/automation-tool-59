import re
from typing import Any, Optional

class AddressValidator:
    ETH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
    BTC_PATTERN = re.compile(r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$')

    @staticmethod
    def is_valid_eth(address: str) -> bool:
        return bool(AddressValidator.ETH_PATTERN.match(address))

    @staticmethod
    def is_valid_btc(address: str) -> bool:
        return bool(AddressValidator.BTC_PATTERN.match(address))

class DataValidator:
    @staticmethod
    def validate_positive_float(value: Any) -> float:
        try:
            val = float(value)
            if val <= 0:
                raise ValueError('Value must be positive')
            return val
        except (TypeError, ValueError):
            raise ValueError(f'Invalid numeric input: {value}')

    @staticmethod
    def validate_ticker(ticker: str) -> str:
        if not isinstance(ticker, str) or not 2 <= len(ticker) <= 10:
            raise ValueError('Invalid ticker format')
        return ticker.upper()

class TransactionValidator:
    @staticmethod
    def check_min_amount(amount: float, min_val: float = 0.0001) -> bool:
        return amount >= min_val