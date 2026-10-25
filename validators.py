import re

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
SOL_ADDRESS_PATTERN = re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")
TX_HASH_PATTERN = re.compile(r"^(0x)?[a-fA-F0-9]{64}$")


def is_valid_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def is_valid_solana_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(SOL_ADDRESS_PATTERN.match(address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    return bool(TX_HASH_PATTERN.match(tx_hash))


def validate_slippage(slippage: float) -> bool:
    if not isinstance(slippage, (int, float)):
        return False
    return 0.0 < slippage <= 50.0


def validate_trade_amount(amount: float, min_amount: float = 0.0) -> bool:
    if not isinstance(amount, (int, float)):
        return False
    return amount > min_amount
