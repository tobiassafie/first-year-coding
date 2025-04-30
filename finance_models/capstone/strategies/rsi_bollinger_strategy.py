# strategies/rsi_bollinger_strategy.py

import pandas as pd
import numpy as np

def generate_signals(df, rsi_window=14, bollinger_window=20, num_std_dev=2):
    """
    RSI + Bollinger Bands Strategy:
    Buy when RSI is oversold AND price touches/below Lower Band.
    Sell when RSI is overbought AND price touches/above Upper Band.

    Args:
        df (DataFrame): must contain a 'Close' price column.
        rsi_window (int): periods for RSI (default=14).
        bollinger_window (int): periods for Bollinger Bands SMA (default=20).
        num_std_dev (float): number of standard deviations for Bollinger Bands (default=2).

    Returns:
        DataFrame: original df with 'Signal' and 'Position' columns added.
    """

    # Calculate Bollinger Bands
    df['SMA'] = df['Close'].rolling(window=bollinger_window).mean()
    df['STDDEV'] = df['Close'].rolling(window=bollinger_window).std()
    df['Upper_Band'] = df['SMA'] + (num_std_dev * df['STDDEV'])
    df['Lower_Band'] = df['SMA'] - (num_std_dev * df['STDDEV'])

    # Calculate RSI
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=rsi_window, min_periods=rsi_window).mean()
    avg_loss = loss.rolling(window=rsi_window, min_periods=rsi_window).mean()

    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Initialize Signal column
    df['Signal'] = 0

    # Buy when Buy Condition becomes newly true
    buy_signal = (df['RSI'] < 30) & (df['Close'] <= df['Lower_Band'])
    sell_signal = (df['RSI'] > 70) & (df['Close'] >= df['Upper_Band'])

    # Entry only on transition
    df.loc[(buy_signal) & (~(buy_signal.shift(1).fillna(False))), 'Signal'] = 1
    df.loc[(sell_signal) & (~(sell_signal.shift(1).fillna(False))), 'Signal'] = -1

    # Forward fill Position
    df['Position'] = df['Signal']
    df['Position'] = df['Position'].ffill()

    # Build Position column by forward-filling signals
    df['Position'] = df['Signal'].replace(to_replace=0, method='ffill')

    # Define warm-up window for plotting purposes
    warmup_window = max(rsi_window, bollinger_window)

    return df, warmup_window
