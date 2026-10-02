import os
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class AppConfig:
    API_URL: str = os.getenv("API_URL", "https://api.exchange.com")
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30"))
    MAX_RETRIES: int = 3
    LOG_LEVEL: str = "INFO"

    def validate(self) -> None:
        if not self.API_URL.startswith("https://"):
            raise ValueError("Invalid API_URL protocol")

class ConfigLoader:
    @staticmethod
    def load() -> AppConfig:
        cfg = AppConfig()
        cfg.validate()
        return cfg

SETTINGS: Final = ConfigLoader.load()