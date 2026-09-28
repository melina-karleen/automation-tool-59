import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def validate_trade_data(data: Dict[str, Any]) -> bool:
    required = {'symbol', 'amount', 'price'}
    if not all(k in data for k in required):
        return False
    if data['amount'] <= 0 or data['price'] <= 0:
        return False
    return isinstance(data['symbol'], str)

def process_stream(data_stream: list) -> None:
    for entry in data_stream:
        try:
            if not validate_trade_data(entry):
                logger.warning(f"invalid trade packet skipped: {entry}")
                continue
            
            execute_trade(entry)
        except Exception as e:
            logger.error(f"processing failure: {e}")

def execute_trade(data: Dict[str, Any]) -> None:
    # Placeholder for exchange integration logic
    logger.info(f"executing {data['symbol']} order")

if __name__ == "__main__":
    mock_data = [
        {'symbol': 'BTC', 'amount': 0.1, 'price': 50000},
        {'symbol': 'ETH', 'amount': -1, 'price': 3000},
        {'symbol': 'SOL', 'amount': 5, 'price': 100}
    ]
    process_stream(mock_data)