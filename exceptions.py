class AutomationError(Exception):
    """Base exception for automation-tool-59."""

class NetworkTimeoutError(AutomationError):
    """Raised when external crypto API request times out."""

class InsufficientFundsError(AutomationError):
    """Raised when wallet balance is below transaction requirement."""

class RateLimitError(AutomationError):
    """Raised when exchange API returns 429 status codes."""

class InvalidSignatureError(AutomationError):
    """Raised when cryptographic signature verification fails."""

def handle_critical_failure(error: Exception) -> None:
    """Centralized diagnostic reporting for automation runtime."""
    import logging

    logger = logging.getLogger("automation-tool-59")
    error_type = type(error).__name__
    
    if isinstance(error, (NetworkTimeoutError, RateLimitError)):
        logger.warning(f"Recoverable {error_type} encountered: {error}")
    elif isinstance(error, (InsufficientFundsError, InvalidSignatureError)):
        logger.error(f"Critical runtime failure: {error_type} - {error}")
    else:
        logger.critical(f"Unhandled system exception: {error_type} - {error}")

    if isinstance(error, AutomationError):
        return
    raise