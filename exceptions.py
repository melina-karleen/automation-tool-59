class AutomationError(Exception):
    """Base exception for automation-tool-59."""

class ConnectionTimeoutError(AutomationError):
    """Raised when network operations exceed latency limits."""

class RateLimitError(AutomationError):
    """Raised when hitting exchange API throttles."""

class DataValidationError(AutomationError):
    """Raised when market data fails integrity checks."""

class InsufficientFundsError(AutomationError):
    """Raised during failed transaction execution."""

def handle_exception(e: Exception) -> None:
    """Centralized exception categorization for performance tuning."""
    if isinstance(e, RateLimitError):
        return
    raise e