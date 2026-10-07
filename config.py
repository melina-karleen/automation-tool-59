import os
from typing import Final
from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkConfig:
    RPC_URL: str = os.getenv("RPC_URL", "https://eth.llamarpc.com")
    CHAIN_ID: int = int(os.getenv("CHAIN_ID", 1))
    TIMEOUT: int = 30

@dataclass(frozen=True)
class APIConfig:
    API_KEY: str = os.getenv("API_KEY", "")
    SECRET: str = os.getenv("SECRET", "")
    RATE_LIMIT: int = 5

class Config:
    NETWORK: Final = NetworkConfig()
    API: Final = APIConfig()
    DEBUG: Final = os.getenv("DEBUG", "false").lower() == "true"

def validate_env() -> None:
    if not Config.API.API_KEY:
        raise EnvironmentError("API_KEY missing in environment variables")