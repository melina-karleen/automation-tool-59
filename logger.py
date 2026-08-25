import time
import random
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, initial_delay=1.0, backoff_factor=2.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            delay = initial_delay
            while attempt < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    attempt += 1
                    if attempt == max_attempts:
                        logger.error(f"Operation failed after {max_attempts} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds")
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator

@retry_network_operation(max_attempts=5, initial_delay=0.5)
def get_crypto_balance(address):
    if random.random() < 0.6:
        raise ConnectionError("Failed to connect to blockchain node")
    return {"address": address, "balance": 1.2345}

if __name__ == "__main__":
    try:
        balance = get_crypto_balance("0x123abc")
        print(balance)
    except Exception as e:
        print(f"Final error: {e}")