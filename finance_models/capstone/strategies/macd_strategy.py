# macd_strategy.py

import pandas as pd
import numpy as np

def generate_signals(df, short_window=12, long_window=26, signal_window=9):
    """
    Generate MACD crossover trading signals.

    Parameters:
    - df: DataFrame with 'Close' prices
    - short_window: period for the short-term EMA (default=12)
    - long_window: period for the long-term EMA (default=26)
    - signal_window: period for the MACD Signal line (default=9)

    Returns:
    - df: DataFrame with added columns ['MACD', 'Signal_Line', 'Position', 'Signal']
    - warmup_window: int, maximum window needed for indicators to warm up
    """

    # Short EMA and Long EMA
    df['Short_EMA'] = df['Close'].ewm(span=short_window, adjust=False).mean()
    df['Long_EMA'] = df['Close'].ewm(span=long_window, adjust=False).mean()

    # MACD Line
    df['MACD'] = df['Short_EMA'] - df['Long_EMA']

    # Signal Line
    df['Signal_Line'] = df['MACD'].ewm(span=signal_window, adjust=False).mean()

    # Create Signal Column
    df['Signal'] = 0
    df.loc[(df['MACD'] > df['Signal_Line']) & (df['MACD'].shift(1) <= df['Signal_Line'].shift(1)), 'Signal'] = 1
    df.loc[(df['MACD'] < df['Signal_Line']) & (df['MACD'].shift(1) >= df['Signal_Line'].shift(1)), 'Signal'] = -1

    # Position (for cumulative returns)
    df['Position'] = df['Signal'].replace(to_replace=0, method='ffill')

    # Calculate warmup window
    warmup_window = max(short_window, long_window, signal_window)

    return df, warmup_window