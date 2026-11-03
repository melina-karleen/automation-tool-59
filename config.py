import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://cloudflare-eth.com",
    "timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.1,
    "slippage_tolerance": 0.5,
    "enable_dry_run": True,
    "symbols": ["BTC/USDT", "ETH/USDT"],
}


class ConfigManager:
    def __init__(self, config_file: str = "config.json") -> None:
        self.config_path = Path(config_file)
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self.config.update(file_config)
            except (json.JSONDecodeError, IOError) as err:
                raise RuntimeError(f"Failed to load config file: {err}") from err

        self._override_from_env()
        return self.config

    def _override_from_env(self) -> None:
        env_mappings = {
            "CRYPTO_NETWORK": ("network", str),
            "CRYPTO_RPC_URL": ("rpc_url", str),
            "CRYPTO_TIMEOUT": ("timeout", int),
            "CRYPTO_DRY_RUN": ("enable_dry_run", lambda v: v.lower() in ("true", "1", "yes")),
        }
        for env_var, (config_key, parser) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                self.config[config_key] = parser(val)

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
