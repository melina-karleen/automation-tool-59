import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass
class Config:
    api_key: str = ""
    api_secret: str = ""
    exchange: str = "binance"
    trading_pair: str = "BTC/USDT"
    max_position_size: float = 0.1
    slippage_tolerance: float = 0.005
    log_level: str = "INFO"
    extra: Dict[str, Any] = field(default_factory=dict)


def load_config(config_path: Optional[Path] = None) -> Config:
    defaults = Config()
    loaded_data: Dict[str, Any] = {}

    if config_path and config_path.is_file():
        with open(config_path, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)

    return Config(
        api_key=os.getenv("CRYPTO_API_KEY", loaded_data.get("api_key", defaults.api_key)),
        api_secret=os.getenv("CRYPTO_API_SECRET", loaded_data.get("api_secret", defaults.api_secret)),
        exchange=loaded_data.get("exchange", os.getenv("CRYPTO_EXCHANGE", defaults.exchange)),
        trading_pair=loaded_data.get("trading_pair", defaults.trading_pair),
        max_position_size=float(loaded_data.get("max_position_size", defaults.max_position_size)),
        slippage_tolerance=float(loaded_data.get("slippage_tolerance", defaults.slippage_tolerance)),
        log_level=loaded_data.get("log_level", defaults.log_level),
        extra=loaded_data.get("extra", {}),
    )
