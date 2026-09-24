import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "max_retries": 3,
    "timeout": 30,
    "gas_strategy": "aggressive"
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.settings = DEFAULT_CONFIG.copy()
        self._load_from_file()

    def _load_from_file(self) -> None:
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                try:
                    user_config = json.load(f)
                    self.settings.update(user_config)
                except json.JSONDecodeError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]