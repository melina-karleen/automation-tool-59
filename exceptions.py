class AutomationError(Exception):
    """Base exception for automation-tool-59."""

class ExchangeConnectionError(AutomationError):
    """Raised when exchange API is unreachable."""

class RateLimitError(AutomationError):
    """Raised when API rate limits are exceeded."""

class OrderExecutionError(AutomationError):
    """Raised when an order placement fails."""

class InsufficientFundsError(AutomationError):
    """Raised when balance is lower than required."""

class ValidationError(AutomationError):
    """Raised when input parameters fail schema checks."""

class ConfigurationError(AutomationError):
    """Raised when environment configuration is missing."""

def handle_exception(exc: Exception) -> None:
    if isinstance(exc, (ExchangeConnectionError, RateLimitError)):
        # Log temporary issues
        return
    if isinstance(exc, (InsufficientFundsError, ValidationError)):
        # Log critical logic issues
        raise exc
    raise exc