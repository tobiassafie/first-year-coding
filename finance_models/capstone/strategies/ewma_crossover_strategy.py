# strategies/ewma_crossover_strategy.py

import pandas as pd

def generate_signals(df, short_window=12, long_window=26):
    """
    EWMA Crossover Strategy:
    Buy when short-term EWMA crosses above long-term EWMA.
    Sell when short-term EWMA crosses below long-term EWMA.

    Args:
        df (DataFrame): must contain a 'Close' price column.
        short_window (int): periods for short EWMA (default=12).
        long_window (int): periods for long EWMA (default=26).

    Returns:
        DataFrame: original df with 'Signal' and 'Position' columns added.
    """

    # Calculate EWMAs
    df['EWMA_Short'] = df['Close'].ewm(span=short_window, adjust=False).mean()
    df['EWMA_Long'] = df['Close'].ewm(span=long_window, adjust=False).mean()

    # Initialize Signal column
    df['Signal'] = 0

    # Generate Buy/Sell signals
    buy_signal = (df['EWMA_Short'] > df['EWMA_Long']) & (~(df['EWMA_Short'].shift(1) > df['EWMA_Long'].shift(1)))
    sell_signal = (df['EWMA_Short'] < df['EWMA_Long']) & (~(df['EWMA_Short'].shift(1) < df['EWMA_Long'].shift(1)))

    df.loc[buy_signal, 'Signal'] = 1
    df.loc[sell_signal, 'Signal'] = -1

    # Build Position column by forward-filling signals
    df['Position'] = df['Signal'].replace(to_replace=0, method='ffill')

    # Define warm-up window for plotting purposes
    warmup_window = max(short_window, long_window)

    return df, warmup_window
