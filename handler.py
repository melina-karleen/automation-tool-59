import logging
from typing import Dict, Any
from .exceptions import CryptoProcessingError

class CryptoHandler:
    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings
        self.logger = logging.getLogger(__name__)

    def process_event(self, data: Dict[str, Any]) -> bool:
        try:
            if not self._validate_payload(data):
                return False
            return self._execute_trade(data)
        except Exception as e:
            self.logger.error(f"execution failed: {e}")
            raise CryptoProcessingError(f"trade failed: {e}")

    def _validate_payload(self, data: Dict[str, Any]) -> bool:
        required = {'pair', 'amount', 'side'}
        return all(key in data for key in required)

    def _execute_trade(self, data: Dict[str, Any]) -> bool:
        self.logger.info(f"executing {data['side']} order for {data['pair']}")
        return True

def initialize_handler(config: Dict[str, Any]) -> CryptoHandler:
    return CryptoHandler(config)