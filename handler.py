import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def validate_trade_data(data: Dict[str, Any]) -> bool:
    required = {'symbol', 'amount', 'price', 'side'}
    if not all(key in data for key in required):
        return False
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return False
    if data['side'] not in {'buy', 'sell'}:
        return False
    return True

def process_queue(queue: list):
    while queue:
        payload = queue.pop(0)
        if not validate_trade_data(payload):
            logger.error(f"invalid payload received: {payload}")
            continue
        try:
            execute_order(payload)
        except Exception as e:
            logger.error(f"execution failed: {e}")

def execute_order(data: Dict[str, Any]):
    logger.info(f"executing {data['side']} order for {data['symbol']}")