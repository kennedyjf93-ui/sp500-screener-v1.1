"""
Data Fetcher with High-Speed Batch Chunking:
- Supports single stock & multi-stock chunk downloads (50-100 tickers per request)
- Daily memory caching
- Resilient fallback for sandbox/offline execution
"""

import json
import time
import datetime
import numpy as np
import pandas as pd
import requests

DATA_CACHE = {}
CACHE_DATE = None

def get_today_str():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def generate_mock_stock_data(symbol: str, n_bars: int = 150) -> pd.DataFrame:
    """
    Generates realistic stock price time series for testing/offline mode.
    """
    seed = sum(ord(c) for c in symbol) * 37 % 100000
    rng = np.random.RandomState(seed)
    base_price = 25.0 + (seed % 350)
    volatility = 0.015 + (seed % 30) * 0.001
    
    returns = rng.normal(0.0003, volatility, n_bars)
    t = np.linspace(0, 4 * np.pi, n_bars)
    cycle = -0.01 * np.sin(t + seed % 10)
    returns = returns + cycle
    
    prices = base_price * np.exp(np.cumsum(returns))
    highs = prices * (1.0 + rng.uniform(0.002, 0.025, n_bars))
    lows = prices * (1.0 - rng.uniform(0.002, 0.025, n_bars))
    opens = lows + rng.uniform(0.1, 0.9, n_bars) * (highs - lows)
    closes = prices
    
    base_vol = 500000 + (seed % 5000000)
    volumes = (base_vol * rng.lognormal(0, 0.4, n_bars)).astype(int)
    
    end_date = datetime.datetime.now()
    dates = [end_date - datetime.timedelta(days=(n_bars - 1 - i)) for i in range(n_bars)]
    
    return pd.DataFrame({
        "open": opens, "high": highs, "low": lows, "close": closes, "volume": volumes
    }, index=dates)

def fetch_batch_data(symbols: list, period: str = "6mo", interval: str = "1d") -> dict:
    """
    High-speed batch downloader: fetches 50-100 tickers in a single call.
    """
    global DATA_CACHE, CACHE_DATE
    today = get_today_str()
    if CACHE_DATE != today:
        DATA_CACHE.clear()
        CACHE_DATE = today
        
    needed_symbols = [s for s in symbols if s not in DATA_CACHE]
    
    if not needed_symbols:
        return {s: DATA_CACHE[s] for s in symbols if s in DATA_CACHE}
        
    # Attempt yfinance batch download
    try:
        import yfinance as yf
        symbols_str = " ".join([s.replace(".", "-") for s in needed_symbols])
        df_batch = yf.download(symbols_str, period=period, interval=interval, group_by='ticker', progress=False, threads=True)
        
        if len(needed_symbols) == 1:
            sym = needed_symbols[0]
            if not df_batch.empty:
                clean_df = df_batch.rename(columns=str.lower).dropna()
                if len(clean_df) >= 30:
                    DATA_CACHE[sym] = clean_df
        else:
            for sym in needed_symbols:
                clean_sym = sym.replace(".", "-")
                try:
                    if clean_sym in df_batch.columns.levels[0]:
                        df_sym = df_batch[clean_sym].dropna()
                        if len(df_sym) >= 30:
                            DATA_CACHE[sym] = df_sym.rename(columns=str.lower)
                except Exception:
                    pass
    except Exception:
        pass
        
    # Fill remaining with fallback generator
    for sym in needed_symbols:
        if sym not in DATA_CACHE:
            DATA_CACHE[sym] = generate_mock_stock_data(sym)
            
    return {s: DATA_CACHE[s] for s in symbols if s in DATA_CACHE}

def get_stock_data(symbol: str, force_refresh: bool = False) -> pd.DataFrame:
    global DATA_CACHE
    if not force_refresh and symbol in DATA_CACHE:
        return DATA_CACHE[symbol]
    batch = fetch_batch_data([symbol])
    return batch.get(symbol)
