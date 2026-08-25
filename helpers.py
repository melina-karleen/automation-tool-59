import re
from typing import Dict

def is_valid_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    address = address.lower().strip()
    if not address.startswith("0x") or len(address) != 42:
        return False
    return bool(re.match(r"^0x[0-9a-f]{40}$", address))

def to_wei(amount: float, decimals: int = 18) -> int:
    return int(amount * (10 ** decimals))

def from_wei(amount: int, decimals: int = 18) -> float:
    return amount / (10 ** decimals)

def calculate_amount_with_slippage(amount: float, slippage_percent: float) -> float:
    return amount * (1 - slippage_percent / 100)

def get_token_decimals(token_symbol: str) -> int:
    decimals: Dict[str, int] = {
        "eth": 18,
        "weth": 18,
        "usdt": 6,
        "usdc": 6,
        "dai": 18,
        "bnb": 18,
        "matic": 18,
    }
    return decimals.get(token_symbol.lower(), 18)

def format_amount(amount: float, precision: int = 4) -> str:
    return f"{amount:.{precision}f}"

def parse_amount(amount_str: str) -> float:
    try:
        return float(amount_str.replace(",", "").strip())
    except (ValueError, AttributeError):
        return 0.0

def get_rpc_url(network: str) -> str:
    rpc_urls: Dict[str, str] = {
        "ethereum": "https://eth.llamarpc.com",
        "bsc": "https://bsc-dataseed.binance.org",
        "polygon": "https://polygon-rpc.com",
    }
    return rpc_urls.get(network.lower(), "")
