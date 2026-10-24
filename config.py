import os
from typing import Dict, Any

class ConfigError(Exception):
    pass

def load_config() -> Dict[str, Any]:
    try:
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        env = os.getenv("ENV", "production")

        if not all([api_key, api_secret]):
            raise ConfigError("missing required credentials")

        return {
            "api_key": api_key,
            "api_secret": api_secret,
            "env": env,
            "rate_limit": int(os.getenv("RATE_LIMIT", 100)),
            "timeout": float(os.getenv("TIMEOUT", 30.0))
        }
    except (ValueError, TypeError) as e:
        raise ConfigError(f"invalid environment variable format: {e}")
    except Exception as e:
        raise ConfigError(f"unexpected configuration failure: {e}")

config = load_config()