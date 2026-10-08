import json
import logging
import time
import urllib.error
import urllib.request

logger = logging.getLogger("automation_tool.utils")


def fetch_crypto_price(symbol: str, max_retries: int = 3, base_delay: float = 1.0) -> float:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    delay = base_delay

    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "CryptoBot"})
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode())
                return float(data["price"])
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(delay * 2)
            elif e.code == 400:
                raise ValueError(f"Invalid trading pair: {symbol}") from e
            else:
                logger.warning(f"HTTP error {e.code} on attempt {attempt + 1}")
        except (urllib.error.URLError, TimeoutError) as e:
            logger.warning(f"Network connection failure: {e}")
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            raise ValueError(f"Malformed API response structure: {e}") from e

        time.sleep(delay)
        delay *= 2.0

    raise ConnectionError(f"Max retries reached for fetching {symbol} price")
