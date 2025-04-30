# **Capstone Quant Simulator**

A modular Python trading simulator that combines a backtesting engine with an interactive trading game. Supports technical indicators including MACD, RSI+Bollinger, and ATR Breakout. Built for experimentation, visualization, and foundational learning in algorithmic trading and quantitative modeling.

---

## **Features**

- Backtesting engine for historical equity data
- Interactive game mode that simulates live trading decisions
- Plug-and-play architecture for new or custom indicators
- Clear trade signal visualizations over price data
- Basic performance tracking and return analytics

---

## **Project Structure**

```bash
trading-simulator/
├── Capstone_Backtester.ipynb        # Core backtesting logic
├── Capstone_Game.ipynb              # Interactive simulation game
├── game_scripts/                    # Modular scripts for game logic and mechanics
│   └── ...
├── strategies/                      # Custom trading algorithms and indicators
│   └── ...
├── media/                           # Screenshots, plots, and visualizations
│   └── ...
├── dev_notebooks/                   # Experimental notebooks for indicator and model development
│   └── ...
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## **How to Run**

```bash
# Clone the repository
git clone https://github.com/tobiassafie/first-year-coding.git
cd first-year-coding/finance_model/capstone

# Install dependencies
pip install -r requirements.txt

# Run the backtester
python Capstone_Backtester.ipynb  # or run in Jupyter Lab/Notebook

# Run the game simulation
python Capstone_Game.ipynb  # or run in Jupyter Lab/Notebook
```
