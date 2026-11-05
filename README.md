[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# automation-tool-59

An automated multi-DEX arbitrage and liquidity management engine designed for EVM-compatible networks. It monitors real-time mempool transactions and decentralized exchange order books to execute low-latency trades with dynamic slippage protection.

## Features

- **Multi-DEX Price Aggregation:** Simultaneously tracks token pair discrepancies across Uniswap V3, Sushiswap, and Curve Finance using WebSockets.
- **Flash Loan Integration:** Executes zero-capital arbitrage transactions by routing calls through Aave V3 pool providers within a single block.
- **MEV Protection:** Protects transactions from front-running and sandwich attacks by utilizing Flashbots private RPC relays.
- **Dynamic Gas Pricing:** Automatically calculates optimal priority fees using EIP-1559 models to ensure target block inclusion without overpaying.

## Installation

Clone the repository and set up the Python environment:

```bash
git clone https://github.com/Developer/automation-tool-59.git
cd automation-tool-59
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set up environment variables:

```bash
cp .env.example .env
```

## Basic Usage

Run the bot using Python after configuring your RPC endpoints:

```python
from automation_tool import ArbitrageEngine, StrategyConfig

config = StrategyConfig(
    network="ethereum",
    rpc_url="https://eth-mainnet.g.alchemy.com/v2/demo",
    target_pairs=["WETH/USDC", "WBTC/WETH"],
    min_profit_threshold_usd=15.50,
    enable_flashbots=True
)

engine = ArbitrageEngine(config)
engine.start_monitoring()
```

To execute a dry-run simulation on a local fork:

```bash
python main.py --mode simulate --fork-block 18500000
```

## License

Distributed under the MIT License. See `LICENSE` for more information.