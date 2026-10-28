import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
    name: str = "crypto_bot",
    log_dir: str = "logs",
    level: int = logging.INFO,
    max_bytes: int = 10_000_000,
    backup_count: int = 5,
) -> logging.Logger:
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    log_file = os.path.join(log_dir, f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_trade_logger(symbol: str) -> logging.Logger:
    clean_symbol = symbol.lower().replace("/", "_")
    return setup_logger(name=f"trade_{clean_symbol}")
