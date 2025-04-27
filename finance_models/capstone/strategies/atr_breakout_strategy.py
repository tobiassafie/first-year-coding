# atr_breakout_strategy.py

import pandas as pd
import numpy as np

def generate_signals(df, scale_factor=0.5, atr_window=14, breakout_window=20):
    """
    Generate ATR Breakout trading signals.

    Parameters:
    - df: DataFrame with 'High', 'Low', 'Close' prices
    - atr_window: period for ATR calculation (default=14)
    - breakout_window: period for recent high/low breakout (default=20)

    Returns:
    - df: DataFrame with added columns ['ATR', 'Upper_Breakout', 'Lower_Breakout', 'Signal', 'Position']
    - warmup_window: int, maximum window needed for indicators to warm up
    """

    # True Range components
    df['High_Low'] = df['High'] - df['Low']
    df['High_Close_Prev'] = np.abs(df['High'] - df['Close'].shift(1))
    df['Low_Close_Prev'] = np.abs(df['Low'] - df['Close'].shift(1))

    # True Range
    df['TR'] = df[['High_Low', 'High_Close_Prev', 'Low_Close_Prev']].max(axis=1)

    # Average True Range (ATR)
    df['ATR'] = df['TR'].rolling(window=atr_window, min_periods=atr_window).mean()

    # 20-Day Highs and Lows
    df['20D_High'] = df['Close'].rolling(window=breakout_window).max()
    df['20D_Low'] = df['Close'].rolling(window=breakout_window).min()

    # Breakout Levels
    df['Upper_Breakout'] = df['20D_High'] + scale_factor * df['ATR']
    df['Lower_Breakout'] = df['20D_Low'] - scale_factor * df['ATR']

    # Initialize Signals
    df['Signal'] = 0

    # Buy Signal: today's Close > yesterday's Upper Breakout, yesterday's Close <= two days ago's Upper Breakout
    buy_condition = (df['Close'] > df['Upper_Breakout'].shift(1)) & (df['Close'].shift(1) <= df['Upper_Breakout'].shift(2))
    df.loc[buy_condition, 'Signal'] = 1

    # Sell Signal: today's Close < yesterday's Lower Breakout, yesterday's Close >= two days ago's Lower Breakout
    sell_condition = (df['Close'] < df['Lower_Breakout'].shift(1)) & (df['Close'].shift(1) >= df['Lower_Breakout'].shift(2))
    df.loc[sell_condition, 'Signal'] = -1


    # Position (carry forward)
    df['Position'] = df['Signal'].replace(to_replace=0, method='ffill')

    # Determine Warmup Window
    warmup_window = max(atr_window, breakout_window)

    return df, warmup_window
