"""
Streamlit Web App for Multi-Index Custom Indicator Screener (High-Speed Batch Mode)
Supports:
- Nasdaq Composite Full (IXIC - 3,390 Stocks)
- S&P 500 (SPX - 503 Stocks)
- Nasdaq 100 (Nas100 - 101 Stocks)
- Dow Jones 30 (DJI - 30 Stocks)
Deployable with 1-click on Streamlit Cloud (https://share.streamlit.io)
"""

import time
import pandas as pd
import numpy as np
import streamlit as st
from concurrent.futures import ThreadPoolExecutor, as_completed

from market_universes import MARKET_UNIVERSES, get_universe_components
from data_fetcher import fetch_batch_data, get_stock_data
from indicator import calculate_indicator_series, get_latest_metrics

st.set_page_config(
    page_title="Multi-Index Stock Screener | IXIC, SPX, Nas100, DJI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title { font-size: 28px; font-weight: 800; color: #26a69a; margin-bottom: 2px; }
    .sub-title { font-size: 14px; color: #888; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📈 Multi-Index Custom Indicator Stock Screener</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">High-Speed Batch Screener for Nasdaq Composite (3,390 Stocks), S&P 500, Nas100, and DJI</div>', unsafe_allow_html=True)

# ----------------- SIDEBAR CONTROLS -----------------
st.sidebar.header("🎯 Market Universe")

universe_options = [
    "Nasdaq Composite Full (IXIC - 3,390 Stocks)",
    "S&P 500 (SPX - 503 Stocks)",
    "Nasdaq 100 (Nas100 - 101 Stocks)",
    "Dow Jones 30 (DJI - 30 Stocks)"
]
selected_universe = st.sidebar.selectbox(
    "Select Stock Index / Market Pool",
    universe_options,
    index=0,
    help="Choose which index universe to scan."
)

base_stocks = get_universe_components(selected_universe)

st.sidebar.markdown("---")
st.sidebar.header("🔍 Screening Filters")

# 1. Minimum Green Bar Depth Slider
min_green = st.sidebar.slider(
    "Minimum Green Bar Value",
    min_value=0.1,
    max_value=9.0,
    value=1.0,
    step=0.1,
    help="Filters stocks where current green bar depth/magnitude >= this value."
)

# 2. Minimum Volume Filter (Useful for IXIC 3,390 stocks)
min_vol_options = {
    "Any Volume (Show All)": 0,
    "≥ 50,000 shares/day": 50000,
    "≥ 100,000 shares/day (Recommended)": 100000,
    "≥ 500,000 shares/day (High Liquidity)": 500000,
    "≥ 1,000,000 shares/day (Mega Liquidity)": 1000000
}
selected_min_vol_label = st.sidebar.selectbox(
    "Liquidity / Min Daily Volume",
    list(min_vol_options.keys()),
    index=2 if "IXIC" in selected_universe else 0,
    help="Filters out low-volume penny stocks."
)
min_vol_threshold = min_vol_options[selected_min_vol_label]

# 3. Sector Selector
available_sectors = ["All"] + sorted(list(set(s["sector"] for s in base_stocks)))
selected_sector = st.sidebar.selectbox("Filter by Sector", available_sectors)

# 4. Signal Filter
signal_filter = st.sidebar.selectbox(
    "Filter by Signals",
    ["All Qualified (Green Bar ≥ Min)", "🟠 Early Buy Signal Only", "🟡 Confirmed Buy Signal Only"]
)

st.sidebar.markdown("---")
st.sidebar.header("⚙️ Indicator Parameters")
with st.sidebar.expander("Adjust Mathematical Weights"):
    w1 = st.slider("Net Volume Weight (w1)", 0.0, 1.0, 0.5, 0.05)
    w2 = st.slider("Mean Reversion Weight (w2)", 0.0, 1.0, 0.5, 0.05)
    nv_len = st.number_input("Volume MA Length", 5, 50, 20)
    norm_len = st.number_input("Lookback Normalization", 20, 200, 100)
    oversold_lvl = st.number_input("Oversold Level", 10.0, 50.0, 35.0)

# ----------------- MAIN ACTION -----------------
short_name = "IXIC (3,390 Stocks)" if "IXIC" in selected_universe else selected_universe.split(" ")[0]
btn_label = f"⚡ START HIGH-SPEED SCREENING ({short_name})"
start_scan = st.button(btn_label, type="primary", use_container_width=True)

if "results" not in st.session_state:
    st.session_state["results"] = None
    st.session_state["universe_used"] = selected_universe

if start_scan:
    stocks = base_stocks if selected_sector == "All" else [s for s in base_stocks if s["sector"] == selected_sector]
    total_stocks = len(stocks)
    
    progress_bar = st.progress(0, text=f"🚀 Preparing high-speed batch download for {total_stocks} stocks...")
    status_text = st.empty()
    
    results = []
    start_time = time.time()
    
    chunk_size = 50
    chunks = [stocks[i:i + chunk_size] for i in range(0, total_stocks, chunk_size)]
    total_chunks = len(chunks)
    scanned_count = 0
    
    for c_idx, chunk in enumerate(chunks):
        chunk_symbols = [s["symbol"] for s in chunk]
        batch_data = fetch_batch_data(chunk_symbols)
        
        for stock_meta in chunk:
            sym = stock_meta["symbol"]
            scanned_count += 1
            df = batch_data.get(sym)
            
            if df is not None and len(df) >= 30:
                last_vol = int(df['volume'].iloc[-1])
                if last_vol >= min_vol_threshold:
                    m = get_latest_metrics(
                        df, symbol=sym, min_threshold=min_green,
                        w1=w1, w2=w2, nv_length=nv_len, norm_len=norm_len, oversold_level=oversold_lvl
                    )
                    if m and m["green_bar_value"] >= min_green:
                        m["name"] = stock_meta["name"]
                        m["sector"] = stock_meta["sector"]
                        m["industry"] = stock_meta["industry"]
                        results.append(m)
                        
        progress = (c_idx + 1) / total_chunks
        progress_bar.progress(progress, text=f"⚡ Batch {c_idx+1}/{total_chunks}: Scanned {scanned_count}/{total_stocks} stocks | Found {len(results)} with Green Bar ≥ {min_green}...")

    elapsed = round(time.time() - start_time, 1)
    progress_bar.empty()
    status_text.success(f"✅ Screening finished in {elapsed}s! Analyzed {scanned_count} stocks across {selected_universe} — Found {len(results)} matching stocks.")
    
    results.sort(key=lambda x: x["green_bar_value"], reverse=True)
    st.session_state["results"] = results
    st.session_state["universe_used"] = selected_universe

# ----------------- DISPLAY RESULTS -----------------
if st.session_state["results"] is not None:
    res = st.session_state["results"]
    
    if signal_filter == "🟠 Early Buy Signal Only":
        res = [r for r in res if r["early_buy_signal"]]
    elif signal_filter == "🟡 Confirmed Buy Signal Only":
        res = [r for r in res if r["confirmed_buy_signal"]]
        
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Qualified Stocks", len(res), help=f"Stocks with Green Bar >= {min_green}")
    with c2:
        top_val = res[0]["green_bar_value"] if len(res) > 0 else 0.0
        st.metric("Highest Green Bar Depth", f"{top_val:.2f} / 10.0")
    with c3:
        early_cnt = sum(1 for r in res if r["early_buy_signal"])
        st.metric("Early Buy Signals (🟠)", early_cnt)
    with c4:
        conf_cnt = sum(1 for r in res if r["confirmed_buy_signal"])
        st.metric("Confirmed Buy Signals (🟡)", conf_cnt)
        
    st.markdown(f"### 📋 Qualified Stocks in **{st.session_state.get('universe_used', 'Index')}**")
    
    if len(res) > 0:
        table_data = []
        for r in res:
            table_data.append({
                "Ticker": r["symbol"],
                "Company Name": r["name"],
                "Sector": r["sector"],
                "Price ($)": f"${r['close']:.2f}",
                "24h Change (%)": f"{r['change_pct']:+.2f}%",
                "Volume": f"{r['volume']:,}",
                "Green Bar Value (0-10)": r["green_bar_value"],
                "Rating": r["rating"],
                "Net Vol Comp": r["norm1"],
                "Mean Rev Comp": r["norm2"],
                "Composite Osc": r["composite"],
                "Early Buy": "🟠 YES" if r["early_buy_signal"] else "—",
                "Confirmed Buy": "🟡 YES" if r["confirmed_buy_signal"] else "—"
            })
            
        df_table = pd.DataFrame(table_data)
        st.dataframe(df_table, use_container_width=True, height=480)
        
        csv_data = df_table.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv_data,
            file_name=f"screener_results_{st.session_state.get('universe_used', 'index')[:4]}.csv",
            mime="text/csv"
        )
        
        st.markdown("---")
        st.markdown("### 🔍 Inspect Individual Stock Chart & Indicator")
        stock_symbols = [r["symbol"] for r in res]
        selected_sym = st.selectbox("Select stock to view chart:", stock_symbols)
        
        selected_stock = next((r for r in res if r["symbol"] == selected_sym), None)
        if selected_stock and "history" in selected_stock:
            hist = selected_stock["history"]
            df_hist = pd.DataFrame(hist)
            df_hist["Date"] = pd.to_datetime(df_hist["time"])
            df_hist.set_index("Date", inplace=True)
            
            c_left, c_right = st.columns(2)
            with c_left:
                st.markdown(f"**{selected_sym} - {selected_stock['name']}**")
                st.markdown(f"Price: **${selected_stock['close']}** ({selected_stock['change_pct']:+.2f}%) | Sector: **{selected_stock['sector']}** | Volume: **{selected_stock['volume']:,}**")
            with c_right:
                st.markdown(f"Green Bar Depth: **{selected_stock['green_bar_value']:.2f} / 10.0** ({selected_stock['rating']})")
                
            st.line_chart(df_hist[["close"]], use_container_width=True)
            st.markdown("**Combined Green Bar Histogram (Lower Pane Magnitude 0–10):**")
            st.bar_chart(df_hist[["combined"]].abs(), use_container_width=True)
    else:
        st.info("No stocks match the current filter. Try lowering the minimum green bar threshold or adjusting volume filters.")
else:
    st.info(f"👋 Ready to scan! Select your desired market index above (**{selected_universe}**) and click the green **START HIGH-SPEED SCREENING** button.")
