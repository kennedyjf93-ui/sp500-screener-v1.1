"""
Indicator Calculation Engine
Exact Mathematical Translation of Pine Script v6:
'Combined Net-Volume + Mean-Reversion Histogram [Custom]'
"""

import numpy as np
import pandas as pd

def calculate_indicator_series(df: pd.DataFrame,
                               nv_length: int = 20,
                               w1: float = 0.5,
                               bb_length: int = 20,
                               bb_mult: float = 2.0,
                               rsi_length: int = 14,
                               stoch_k: int = 14,
                               stoch_d: int = 3,
                               mfi_length: int = 14,
                               comp_smooth: int = 3,
                               w2: float = 0.5,
                               norm_len: int = 100,
                               out_scale: float = 10.0,
                               pivot_bars: int = 3,
                               extreme_frac: float = 0.5,
                               vol_multiplier: float = 1.5,
                               vol_ma_len: int = 20,
                               oversold_level: float = 35.0,
                               overbought_level: float = 65.0,
                               min_confluence: int = 2,
                               early_lookback: int = 2):
    """
    Computes full time series of the indicator.
    """
    close = df['close'].astype(float)
    high = df['high'].astype(float)
    low = df['low'].astype(float)
    volume = df['volume'].astype(float)
    
    # ---------------- Component 1: Net Volume (green-only side) ----------------
    close_diff = close.diff()
    nv = np.where(close_diff > 0, volume, np.where(close_diff < 0, -volume, 0.0))
    cnv = pd.Series(nv, index=df.index).cumsum()
    cnv_sma = cnv.rolling(window=nv_length, min_periods=1).mean()
    cnv_tb = cnv - cnv_sma
    comp1_raw = np.minimum(cnv_tb, 0.0) # negative side survives
    comp1_pos = np.maximum(cnv_tb, 0.0) # mirror side for distribution
    
    # ---------------- Component 2: Mean Reversion momentum (red-only side) ----------------
    # Bollinger Bands %B
    bb_basis = close.rolling(window=bb_length, min_periods=1).mean()
    bb_dev = bb_mult * close.rolling(window=bb_length, min_periods=1).std(ddof=0)
    bb_upper = bb_basis + bb_dev
    bb_lower = bb_basis - bb_dev
    bb_diff = bb_upper - bb_lower
    bb_percent = np.where(bb_diff != 0, (close - bb_lower) / bb_diff * 100.0, 50.0)
    bb_percent = pd.Series(bb_percent, index=df.index)
    
    # RSI (Wilder's smoothing)
    delta = close.diff()
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)
    gain_series = pd.Series(gain, index=df.index)
    loss_series = pd.Series(loss, index=df.index)
    avg_gain = gain_series.ewm(alpha=1.0/rsi_length, min_periods=rsi_length, adjust=False).mean()
    avg_loss = loss_series.ewm(alpha=1.0/rsi_length, min_periods=rsi_length, adjust=False).mean()
    rs = avg_gain / np.where(avg_loss == 0, 1e-9, avg_loss)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    rsi = rsi.fillna(50.0)
    
    # Stochastic %K and %D
    lowest_low = low.rolling(window=stoch_k, min_periods=1).min()
    highest_high = high.rolling(window=stoch_k, min_periods=1).max()
    hl_diff = highest_high - lowest_low
    stoch_k_val = np.where(hl_diff != 0, 100.0 * (close - lowest_low) / hl_diff, 50.0)
    stoch_k_val = pd.Series(stoch_k_val, index=df.index)
    stoch_d_val = stoch_k_val.rolling(window=stoch_d, min_periods=1).mean()
    
    # MFI (Money Flow Index with close and volume)
    typical_price = close
    money_flow = typical_price * volume
    tp_diff = typical_price.diff()
    pos_mf = np.where(tp_diff > 0, money_flow, 0.0)
    neg_mf = np.where(tp_diff < 0, money_flow, 0.0)
    pos_mf_sum = pd.Series(pos_mf, index=df.index).rolling(window=mfi_length, min_periods=1).sum()
    neg_mf_sum = pd.Series(neg_mf, index=df.index).rolling(window=mfi_length, min_periods=1).sum()
    mr = pos_mf_sum / np.where(neg_mf_sum == 0, 1e-9, neg_mf_sum)
    mfi = 100.0 - (100.0 / (1.0 + mr))
    mfi = pd.Series(mfi, index=df.index).fillna(50.0)
    
    # Williams %R
    williams_r = stoch_k_val
    
    # Composite
    composite_raw = (bb_percent + rsi + stoch_d_val + mfi + williams_r) / 5.0
    composite = composite_raw.rolling(window=comp_smooth, min_periods=1).mean()
    
    # Momentum (5 bars)
    histogram = composite.diff(5)
    comp2_raw = np.minimum(histogram.fillna(0.0), 0.0)
    comp2_pos = np.maximum(histogram.fillna(0.0), 0.0)
    
    # ---------------- Unify units: rescale each onto shared axis ----------------
    half = out_scale / 2.0
    
    comp1_series = pd.Series(comp1_raw, index=df.index)
    low1 = comp1_series.rolling(window=norm_len, min_periods=1).min()
    norm1 = np.where(low1 != 0, (comp1_raw / low1) * (-half), 0.0)
    
    comp2_series = pd.Series(comp2_raw, index=df.index)
    low2 = comp2_series.rolling(window=norm_len, min_periods=1).min()
    norm2 = np.where(low2 != 0, (comp2_raw / low2) * (-half), 0.0)
    
    combined = 2.0 * (w1 * norm1 + w2 * norm2)
    combined_series = pd.Series(combined, index=df.index)
    green_bar_magnitude = np.abs(combined_series)
    
    # ---------------- Mirror Distribution Pipeline (combinedTop) ----------------
    comp1_pos_series = pd.Series(comp1_pos, index=df.index)
    high1 = comp1_pos_series.rolling(window=norm_len, min_periods=1).max()
    norm_top1 = np.where(high1 != 0, (comp1_pos / high1) * half, 0.0)
    
    comp2_pos_series = pd.Series(comp2_pos, index=df.index)
    high2 = comp2_pos_series.rolling(window=norm_len, min_periods=1).max()
    norm_top2 = np.where(high2 != 0, (comp2_pos / high2) * half, 0.0)
    
    combined_top = 2.0 * (w1 * norm_top1 + w2 * norm_top2)
    combined_top_series = pd.Series(combined_top, index=df.index)
    
    # ---------------- Volume Ratio & Climax ----------------
    vol_sma = volume.rolling(window=vol_ma_len, min_periods=1).mean()
    vol_ratio = volume / np.where(vol_sma == 0, 1e-9, vol_sma)
    vol_ratio_series = pd.Series(vol_ratio, index=df.index)
    
    # ---------------- Signals Logic ----------------
    # 1. Early Buy Signal (Orange Circle)
    low_combined = combined_series.rolling(window=norm_len, min_periods=1).min()
    early_lookback_min = combined_series.rolling(window=early_lookback, min_periods=1).min()
    early_is_new_low = combined_series <= early_lookback_min
    
    early_factor_depth = (low_combined != 0) & (combined_series <= low_combined * extreme_frac)
    early_factor_climax = vol_ratio_series >= vol_multiplier
    early_factor_oversold = composite <= oversold_level
    
    early_confluence = (
        early_factor_depth.astype(int) + 
        early_factor_climax.astype(int) + 
        early_factor_oversold.astype(int)
    )
    early_buy_signal = early_is_new_low & (early_confluence >= min_confluence)
    
    # 2. Confirmed Buy Signal (Pivot Low)
    is_pivot_low = pd.Series(False, index=df.index)
    combined_arr = combined_series.values
    n = len(combined_arr)
    
    for i in range(pivot_bars, n - pivot_bars):
        val = combined_arr[i]
        left_min = np.min(combined_arr[i - pivot_bars:i])
        right_min = np.min(combined_arr[i + 1:i + pivot_bars + 1])
        if val <= left_min and val <= right_min:
            is_pivot_low.iloc[i + pivot_bars] = True
            
    factor_depth = (low_combined != 0) & (combined_series <= low_combined * extreme_frac)
    factor_climax = vol_ratio_series.rolling(window=pivot_bars * 2 + 1, min_periods=1).max() >= vol_multiplier
    factor_oversold = composite.shift(pivot_bars) <= oversold_level
    
    confirmed_confluence = (
        factor_depth.astype(int) + 
        factor_climax.astype(int) + 
        factor_oversold.astype(int)
    )
    confirmed_buy_signal = is_pivot_low & (confirmed_confluence >= min_confluence)
    
    # 3. Early Sell Signal
    high_combined_top = combined_top_series.rolling(window=norm_len, min_periods=1).max()
    early_lookback_max = combined_top_series.rolling(window=early_lookback, min_periods=1).max()
    early_is_new_high = combined_top_series >= early_lookback_max
    
    early_factor_height = (high_combined_top != 0) & (combined_top_series >= high_combined_top * extreme_frac)
    early_factor_overbought = composite >= overbought_level
    early_sell_confluence = (
        early_factor_height.astype(int) + 
        early_factor_climax.astype(int) + 
        early_factor_overbought.astype(int)
    )
    early_sell_signal = early_is_new_high & (early_sell_confluence >= min_confluence)
    
    result_df = pd.DataFrame({
        'open': df['open'],
        'high': df['high'],
        'low': df['low'],
        'close': df['close'],
        'volume': df['volume'],
        'cnv_tb': cnv_tb,
        'comp1_raw': comp1_raw,
        'comp2_raw': comp2_raw,
        'norm1': norm1,
        'norm2': norm2,
        'combined': combined_series,
        'green_bar_value': green_bar_magnitude,
        'composite': composite,
        'rsi': rsi,
        'mfi': mfi,
        'early_buy_signal': early_buy_signal,
        'confirmed_buy_signal': confirmed_buy_signal,
        'early_sell_signal': early_sell_signal
    }, index=df.index)
    
    return result_df

def get_latest_metrics(df: pd.DataFrame, symbol: str = "", min_threshold: float = 1.0, **kwargs):
    """
    Extracts latest metrics for the screener.
    """
    results = calculate_indicator_series(df, **kwargs)
    if len(results) == 0:
        return None
    
    latest = results.iloc[-1]
    prev = results.iloc[-2] if len(results) >= 2 else latest
    
    close_val = float(latest['close'])
    prev_close = float(prev['close'])
    change_pct = ((close_val - prev_close) / prev_close * 100.0) if prev_close != 0 else 0.0
    
    green_val = round(float(latest['green_bar_value']), 3)
    
    # Qualitative strength rating based on green bar magnitude
    if green_val >= 7.0:
        rating = "Very High (>=7.0)"
        rating_color = "#00E676"
    elif green_val >= 4.0:
        rating = "High (4.0-7.0)"
        rating_color = "#26A69A"
    elif green_val >= 1.0:
        rating = "Moderate (1.0-4.0)"
        rating_color = "#80CBC4"
    else:
        rating = "Low (<1.0)"
        rating_color = "#78909C"
        
    return {
        "symbol": symbol,
        "close": round(close_val, 2),
        "change_pct": round(change_pct, 2),
        "volume": int(latest['volume']),
        "green_bar_value": green_val,
        "has_green_bar": green_val >= min_threshold,
        "norm1": round(float(latest['norm1']), 2),
        "norm2": round(float(latest['norm2']), 2),
        "composite": round(float(latest['composite']), 1),
        "rsi": round(float(latest['rsi']), 1),
        "mfi": round(float(latest['mfi']), 1),
        "early_buy_signal": bool(latest['early_buy_signal']),
        "confirmed_buy_signal": bool(latest['confirmed_buy_signal']),
        "early_sell_signal": bool(latest['early_sell_signal']),
        "rating": rating,
        "rating_color": rating_color,
        "history": [
            {
                "time": d.strftime("%Y-%m-%d") if hasattr(d, "strftime") else str(d),
                "open": round(float(row['open']), 2),
                "high": round(float(row['high']), 2),
                "low": round(float(row['low']), 2),
                "close": round(float(row['close']), 2),
                "volume": int(row['volume']),
                "green_bar_value": round(float(row['green_bar_value']), 3),
                "combined": round(float(row['combined']), 3),
                "composite": round(float(row['composite']), 1),
                "early_buy": bool(row['early_buy_signal']),
                "confirmed_buy": bool(row['confirmed_buy_signal'])
            }
            for d, row in results.tail(60).iterrows()
        ]
    }
