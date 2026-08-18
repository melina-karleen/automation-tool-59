import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger('crypto_tool.log')
    log.info('Logger setup complete.')