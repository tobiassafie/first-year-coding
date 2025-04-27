# strategies/sma_crossover_strategy.py

import pandas as pd

def generate_signals(df, short_window=20, long_window=50):
    """
    SMA Crossover Strategy:
    Buy when short-term SMA crosses above long-term SMA.
    Sell when short-term SMA crosses below long-term SMA.

    Args:
        df (DataFrame): must contain a 'Close' price column.
        short_window (int): periods for short SMA.
        long_window (int): periods for long SMA.

    Returns:
        DataFrame: original df with 'Signal' and 'Position' columns added.
    """

    # Calculate SMAs
    df['SMA_Short'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_Long'] = df['Close'].rolling(window=long_window).mean()

    # Initialize Signal column
    df['Signal'] = 0

    # Generate Buy/Sell signals
    buy_signal = (df['SMA_Short'] > df['SMA_Long']) & (~(df['SMA_Short'].shift(1) > df['SMA_Long'].shift(1)))
    sell_signal = (df['SMA_Short'] < df['SMA_Long']) & (~(df['SMA_Short'].shift(1) < df['SMA_Long'].shift(1)))

    df.loc[buy_signal, 'Signal'] = 1
    df.loc[sell_signal, 'Signal'] = -1

    # Build Position column by forward-filling signals
    df['Position'] = df['Signal'].replace(to_replace=0, method='ffill')

    return df
