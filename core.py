from decimal import Decimal
from typing import Any, Dict, List


class CryptoOrderManager:
    """Manages order calculation and execution tracking for crypto exchanges."""

    def __init__(
        self, api_key: str, secret_key: str, base_url: str = "https://api.exchange.com"
    ) -> None:
        """Initialize the order manager with credentials.

        Args:
            api_key: The exchange API key.
            secret_key: The exchange secret key.
            base_url: Base endpoint URL for the exchange API.
        """
        self.api_key: str = api_key
        self.secret_key: str = secret_key
        self.base_url: str = base_url
        self._order_history: List[Dict[str, Any]] = []

    def calculate_position_size(
        self,
        balance: Decimal,
        risk_percentage: Decimal,
        entry_price: Decimal,
        stop_loss: Decimal,
    ) -> Decimal:
        """Calculate position size based on account balance and risk parameters.

        Args:
            balance: Account balance in quote currency.
            risk_percentage: Risk allowance per trade as decimal (e.g., 0.02).
            entry_price: Target entry price for asset.
            stop_loss: Stop loss execution price.

        Returns:
            Recommended position size in base currency units.
        """
        if entry_price <= Decimal("0") or stop_loss <= Decimal("0"):
            raise ValueError("Prices must be greater than zero.")
        risk_amount: Decimal = balance * risk_percentage
        price_risk: Decimal = abs(entry_price - stop_loss)
        if price_risk == Decimal("0"):
            raise ValueError("Entry price and stop loss cannot be equal.")
        return risk_amount / price_risk

    def create_limit_order(
        self, symbol: str, side: str, amount: Decimal, price: Decimal
    ) -> Dict[str, Any]:
        """Construct and record a limit order payload.

        Args:
            symbol: Asset pair identifier (e.g., 'BTC/USDT').
            side: Order direction ('buy' or 'sell').
            amount: Quantity of base currency to trade.
            price: Limit price for order execution.

        Returns:
            Order payload dict with current status.
        """
        order: Dict[str, Any] = {
            "symbol": symbol.upper(),
            "side": side.lower(),
            "amount": str(amount),
            "price": str(price),
            "status": "pending",
        }
        self._order_history.append(order)
        return order
