import logging
from functools import lru_cache

class CryptoLogger:
    def __init__(self, name: str = "automation-tool-59"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    @lru_cache(maxsize=128)
    def get_logger(self, module_name: str) -> logging.Logger:
        return self.logger.getChild(module_name)

    def info(self, msg: str):
        self.logger.info(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)