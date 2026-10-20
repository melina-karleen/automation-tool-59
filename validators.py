import re
from typing import Any

class CryptoValidator:
    ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

    @staticmethod
    def is_valid_address(address: str) -> bool:
        return bool(CryptoValidator.ADDRESS_PATTERN.match(address))

    @staticmethod
    def validate_amount(amount: Any) -> float:
        try:
            value = float(amount)
            if value <= 0:
                raise ValueError('amount must be positive')
            return value
        except (TypeError, ValueError):
            raise ValueError(f'invalid amount: {amount}')

    @staticmethod
    def sanitize_symbol(symbol: str) -> str:
        if not isinstance(symbol, str):
            raise ValueError('symbol must be string')
        return symbol.strip().upper()

class ConfigValidator:
    @staticmethod
    def validate_network_config(config: dict) -> None:
        required = {'rpc_url', 'chain_id'}
        if not all(k in config for k in required):
            raise KeyError(f'missing required keys: {required - config.keys()}')