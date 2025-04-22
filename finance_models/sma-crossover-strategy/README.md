# SMA Crossover Strategy

This project implements a Simple Moving Average (SMA) crossover strategy to generate buy and sell signals for stock trading.
It can be utilized to analyze an SMA of any window size on any stock + timeframe of your choosing via yfinance.

The model simulates trading using two moving averages:
- **Short SMA** (e.g. 20-day)
- **Long SMA** (e.g. 50-day)

### How It Works
- A **buy** signal is generated when the short SMA crosses **above** the long SMA (golden cross).
- A **sell** signal is generated when the short SMA crosses **below** the long SMA (death cross).
- The simulation tracks portfolio value over time versus a simple buy-and-hold strategy.

### Key Learnings
- The strategy performs well on steady-trending assets like $JPM.
- It underperforms during rapid price increases (e.g. $TSLA in 2020–21), highlighting the lagging nature of SMAs.
- Real-world use requires parameter tuning, validation, and risk management.

### Screenshots from the Model
<img src="../assets/JPM_SMA_buysell.png" alt="JPM 1" width="650">
