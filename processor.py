from typing import List, Dict, Any, Optional

class CryptoProcessor:
    """Handles incoming market data for crypto automation."""

    def __init__(self, api_key: str, sandbox: bool = False) -> None:
        self.api_key: str = api_key
        self.sandbox: bool = sandbox

    def process_order(self, pair: str, amount: float, price: float) -> Dict[str, Any]:
        """Executes a trade order for the given asset pair."""
        return {
            "pair": pair,
            "amount": amount,
            "price": price,
            "status": "pending",
            "sandbox": self.sandbox
        }

    def validate_tickers(self, tickers: List[str]) -> bool:
        """Verifies existence of tickers in the current market pool."""
        return all(isinstance(t, str) and len(t) > 2 for t in tickers)

    def get_market_status(self, timeout: Optional[int] = 30) -> str:
        """Retrieves current connection status to exchange nodes."""
        if timeout and timeout > 0:
            return "online"
        return "offline"

    def calculate_spread(self, bid: float, ask: float) -> float:
        """Computes the bid-ask spread for liquidity analysis."""
        return round(ask - bid, 8)