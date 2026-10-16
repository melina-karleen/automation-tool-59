import logging

class DataProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate_input(self, data: dict) -> bool:
        required = ['symbol', 'amount', 'price']
        if not all(k in data for k in required):
            return False
        if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
            return False
        if not isinstance(data['price'], (int, float)) or data['price'] < 0:
            return False
        return True

    def run_loop(self, queue):
        while True:
            try:
                message = queue.get()
                if message is None:
                    break
                
                if not self.validate_input(message):
                    self.logger.warning(f"invalid payload received: {message}")
                    continue

                self.process(message)
            except Exception as e:
                self.logger.error(f"unexpected processing error: {e}")

    def process(self, data: dict):
        # processing logic implementation
        self.logger.info(f"processing trade for {data['symbol']}")