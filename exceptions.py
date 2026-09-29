class AutomationError(Exception):
    """Base exception for automation-tool-59."""

class ExchangeConnectionError(AutomationError):
    """Raised when connection to the exchange fails."""

class InsufficientFundsError(AutomationError):
    """Raised when wallet balance is below threshold."""

class RateLimitExceeded(AutomationError):
    """Raised when API requests exceed defined limits."""

class OrderExecutionError(AutomationError):
    """Raised when a trade order fails to execute."""

class ConfigurationError(AutomationError):
    """Raised when provided configuration values are invalid."""

def handle_exception(exc: Exception) -> str:
    """Format exception message for logging purposes."""
    return f"[{exc.__class__.__name__}] {str(exc)}"