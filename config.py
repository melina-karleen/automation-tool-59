import json
import os
from typing import Any, Dict

DEFAULTS = {
    "rpc_url": "https://bsc-dataseed.binance.org",
    "max_retries": 3,
    "timeout": 30,
    "gas_multiplier": 1.2
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULTS.copy()
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                user_config = json.load(f)
                config.update(user_config)
            except json.JSONDecodeError:
                pass
    return config

class ConfigManager:
    def __init__(self, path: str = "config.json"):
        self._config = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def settings(self) -> Dict[str, Any]:
        return self._config.copy()