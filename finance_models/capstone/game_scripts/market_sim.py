# title: market_sim.py

import numpy as np
import pandas as pd

stock_catalog = {
    'Minisoft':  {'ticker': 'MSMS',  'category': 'Tech',     'price_range': (100, 400)},
    'Pear'    :  {'ticker': 'PEAR',  'category': 'Tech',     'price_range': (100, 400)},
    'SpillExx':  {'ticker': 'SPXX',  'category': 'Energy',   'price_range': (40,  120)},
    'NewGen Energy': {'ticker': 'NWGN', 'category': 'Energy','price_range': (20,  100)},
    'Cencorp' :  {'ticker': 'CNCP',  'category': 'Pharma',   'price_range': (60,  200)},
    'ModerNay':  {'ticker': 'MODN',  'category': 'Pharma',   'price_range': (60,  200)},
    'Wall Market':  {'ticker': 'WLMT',  'category': 'Retail','price_range': (30,  150)},
    'Sahara'  :  {'ticker': 'SHRA',  'category': 'Retail',   'price_range': (50,  200)},
    'Boom'    :  {'ticker': 'BOOM',  'category': 'Startup',  'price_range': (10,  100)},
    'The Slap':  {'ticker': 'SLAP',  'category': 'Startup',  'price_range': (10,  100)}
}

# -- Main Market Simulation Function --
def market_simulation(days=100):
    """
    Generate fake market data over a number of days, including bull/bear runs.

    Parameters:
    - days (int): number of days to simulate

    Returns:
    - DataFrame: market data with OHLCV and mode info
    """

    stock_data = []

    # Step 1: Initialize starting prices
    starting_prices = {}
    for stock_name, info in stock_catalog.items():
        price_low, price_high = info['price_range']
        start_price = np.random.uniform(price_low, price_high)
        starting_prices[stock_name] = start_price

    # Step 2: Set base parameters
    base_volatility = 0.02  # Random daily movement
    dates = pd.date_range(start='2025-01-01', periods=days)

    # Step 3: Track market modes
    current_mode = {stock: 'neutral' for stock in stock_catalog.keys()}
    mode_timer = {stock: 0 for stock in stock_catalog.keys()}

    for day in range(days):
        current_date = dates[day]

        for stock_name, info in stock_catalog.items():
            ticker = info['ticker']
            prev_close = starting_prices[stock_name]

            # Step 4: Decide bull/bear runs
            if mode_timer[stock_name] == 0:
                # 5% chance to start a new run
                if np.random.rand() < 0.05:
                    new_mode = np.random.choice(['bull', 'bear'])
                    current_mode[stock_name] = new_mode
                    mode_timer[stock_name] = np.random.randint(5, 20)  # Run lasts 5–20 days
                else:
                    current_mode[stock_name] = 'neutral'
            else:
                mode_timer[stock_name] -= 1

            # Step 5: Set drift based on mode
            if current_mode[stock_name] == 'bull':
                drift = 0.001  # Tiny positive drift
            elif current_mode[stock_name] == 'bear':
                drift = -0.001  # Tiny negative drift
            else:
                drift = 0  # Neutral, pure random walk

            # Step 6: Apply drift + noise
            shock = np.random.normal(0, base_volatility)
            new_close = prev_close * (1 + drift + shock)
            new_close = max(new_close, 1)

            # Create realistic OHLC around Close
            open_price = prev_close
            high_price = max(open_price, new_close) * (1 + np.random.uniform(0, 0.01))
            low_price = min(open_price, new_close) * (1 - np.random.uniform(0, 0.01))
            volume = np.random.randint(1000, 10000)

            # Save data
            stock_data.append({
                'Date': current_date,
                'Stock': stock_name,
                'Ticker': ticker,
                'Open': round(open_price, 2),
                'High': round(high_price, 2),
                'Low': round(low_price, 2),
                'Close': round(new_close, 2),
                'Volume': volume,
                'Mode': current_mode[stock_name]  # NEW: track market mode
            })

            # Update stored price
            starting_prices[stock_name] = new_close

    # Step 7: Return as DataFrame
    return pd.DataFrame(stock_data)