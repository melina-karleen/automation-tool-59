import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://eth-mainnet.public.blastapi.io",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO",
    "gas_buffer": 0.001
}

class ConfigLoader:
    def __init__(self, env_prefix: str = "CRYPTO_"):
        self.env_prefix = env_prefix
        self.settings = DEFAULT_CONFIG.copy()
        self._load_from_env()

    def _load_from_env(self) -> None:
        for key in self.settings.keys():
            env_var = f"{self.env_prefix}{key.upper()}"
            value = os.getenv(env_var)
            if value is not None:
                self.settings[key] = self._cast_type(key, value)

    def _cast_type(self, key: str, value: str) -> Any:
        target_type = type(DEFAULT_CONFIG[key])
        try:
            return target_type(value)
        except (ValueError, TypeError):
            return DEFAULT_CONFIG[key]

    def get(self, key: str) -> Any:
        return self.settings.get(key)

config = ConfigLoader()