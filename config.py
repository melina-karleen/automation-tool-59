import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://api.mainnet.chain",
    "timeout": 30,
    "retry_attempts": 3,
    "wallet_address": None
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass
        return config

    def get(self, key: str) -> Any:
        return self.data.get(key)

def get_config() -> ConfigLoader:
    return ConfigLoader()