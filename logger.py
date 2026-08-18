import logging

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        try:
            self.logger.debug(msg)
        except Exception as e:
            self.logger.error(f'Error logging debug message: {e}')

    def info(self, msg):
        try:
            self.logger.info(msg)
        except Exception as e:
            self.logger.error(f'Error logging info message: {e}')

    def warning(self, msg):
        try:
            self.logger.warning(msg)
        except Exception as e:
            self.logger.error(f'Error logging warning message: {e}')

    def error(self, msg):
        try:
            self.logger.error(msg)
        except Exception as e:
            self.logger.error(f'Error logging error message: {e}')

    def critical(self, msg):
        try:
            self.logger.critical(msg)
        except Exception as e:
            self.logger.error(f'Error logging critical message: {e}')