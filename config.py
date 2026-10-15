import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://eth.llamarpc.com",
    "timeout": 30,
    "retries": 3,
    "debug": False
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.settings = self._load()

    def _load(self) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    user_data = json.load(f)
                    config.update(user_data)
            except (json.JSONDecodeError, IOError):
                pass
        return config

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.settings