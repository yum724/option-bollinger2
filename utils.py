
import pandas as pd
import numpy as np

def load_data(file):
    if isinstance(file, str):
        return pd.read_csv(file)
    else:
        return pd.read_csv(file)

def add_indicators(df):
    df['SMA'] = df['Close'].rolling(window=14).mean()
    df['STD'] = df['Close'].rolling(window=14).std()
    df['ボリンジャー_上限'] = df['SMA'] + (2 * df['STD'])
    df['ボリンジャー_下限'] = df['SMA'] - (2 * df['STD'])
    df['RSI'] = compute_rsi(df['Close'])
    df['MACD'] = df['Close'].ewm(span=12).mean() - df['Close'].ewm(span=26).mean()
    return df

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def predict_signal(df):
    signals = []
    for i in range(len(df)):
        if df['Close'].iloc[i] > df['ボリンジャー_上限'].iloc[i] and df['RSI'].iloc[i] > 70:
            signals.append("⬇ PUT")
        elif df['Close'].iloc[i] < df['ボリンジャー_下限'].iloc[i] and df['RSI'].iloc[i] < 30:
            signals.append("⬆ CALL")
        else:
            signals.append("")
    return signals
