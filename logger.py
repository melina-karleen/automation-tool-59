import logging
import sys
from logging.handlers import QueueHandler, QueueListener
from queue import Queue

class AsyncLogger:
    def __init__(self, name: str = "crypto_bot"):
        self.log_queue = Queue(-1)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.queue_handler = QueueHandler(self.log_queue)
        self.logger.addHandler(self.queue_handler)
        
        self.listener = QueueListener(self.log_queue, handler)
        self.listener.start()

    def get_logger(self) -> logging.Logger:
        return self.logger

    def stop(self):
        self.listener.stop()

logger_instance = AsyncLogger()
log = logger_instance.get_logger()