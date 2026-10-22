class AutomationError(Exception):
    """Base exception for automation-tool-59."""

class ConnectionTimeoutError(AutomationError):
    """Raised when exchange API request times out."""

class InsufficientBalanceError(AutomationError):
    """Raised when wallet balance is too low."""

class RateLimitExceeded(AutomationError):
    """Raised when API quota is exhausted."""

class ValidationError(AutomationError):
    """Raised for malformed transaction data."""

import logging

logger = logging.getLogger('automation-tool-59')

def handle_exception(exc: Exception) -> None:
    if isinstance(exc, (ConnectionTimeoutError, RateLimitExceeded)):
        logger.warning(f"Transient error: {exc}")
    elif isinstance(exc, (InsufficientBalanceError, ValidationError)):
        logger.error(f"Critical logic failure: {exc}")
    else:
        logger.critical(f"Unexpected system failure: {exc}")
        raise exc