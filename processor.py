from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Transaction:
    tx_id: str
    amount: float
    symbol: str

class CryptoProcessor:
    """Handles batch processing of crypto transactions."""

    def __init__(self, fee_rate: float = 0.001) -> None:
        self.fee_rate: float = fee_rate

    def calculate_net_amount(self, tx: Transaction) -> float:
        """Calculates amount after network fees."""
        return tx.amount * (1 - self.fee_rate)

    def process_batch(self, transactions: List[Transaction]) -> Dict[str, float]:
        """Processes list of transactions and returns mapping of IDs to net amounts."""
        return {tx.tx_id: self.calculate_net_amount(tx) for tx in transactions}

    def filter_large_txs(self, transactions: List[Transaction], threshold: float) -> List[Transaction]:
        """Filters transactions exceeding specified threshold."""
        return [tx for tx in transactions if tx.amount > threshold]

    def get_summary(self, transactions: List[Transaction]) -> Optional[Dict[str, float]]:
        """Returns summary statistics for a batch."""
        if not transactions:
            return None
        
        total: float = sum(tx.amount for tx in transactions)
        return {
            "total_volume": total,
            "avg_tx": total / len(transactions)
        }