class CryptoError(Exception):
    """Base exception for automation-tool-59."""


class DataParsingError(CryptoError):
    """Raised when ticker data is malformed."""


class ExchangeConnectionError(CryptoError):
    """Raised when exchange API is unreachable."""


class RateLimitError(CryptoError):
    """Raised when API threshold is exceeded."""


def handle_crypto_exception(e: Exception) -> None:
    if isinstance(e, RateLimitError):
        print(f"Rate limit exceeded: {e}")
    elif isinstance(e, DataParsingError):
        print(f"Critical data corruption: {e}")
    else:
        print(f"General operational failure: {e}")


__all__ = [
    "CryptoError",
    "DataParsingError",
    "ExchangeConnectionError",
    "RateLimitError",
    "handle_crypto_exception"
]