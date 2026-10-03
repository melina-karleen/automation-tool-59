import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY: str = os.getenv("API_KEY", "")
    API_SECRET: str = os.getenv("API_SECRET", "")
    BASE_URL: str = "https://api.exchange.com"
    TIMEOUT: int = 30
    MAX_RETRIES: int = 3

    @classmethod
    def validate(cls) -> None:
        if not cls.API_KEY or not cls.API_SECRET:
            raise EnvironmentError("Missing required API credentials")

    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        return {
            "base_url": cls.BASE_URL,
            "timeout": cls.TIMEOUT,
            "max_retries": cls.MAX_RETRIES
        }

def get_config() -> Config:
    Config.validate()
    return Config()