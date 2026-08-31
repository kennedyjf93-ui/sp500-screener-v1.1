"""
Streamlit Web App for S&P 500 Custom Indicator Screener
Deployable with 1-click on Streamlit Cloud (https://share.streamlit.io)
"""

import time
import pandas as pd
import numpy as np
import streamlit as st
from concurrent.futures import ThreadPoolExecutor, as_completed

from sp500 import SP500_COMPONENTS
from data_fetcher import get_stock_data
from indicator import calculate_indicator_series, get_latest_metrics

st.set_page_config(
    page_title="S&P 500 Alpha Screener",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title { font-size: 28px; font-weight: 800; color: #26a69a; margin-bottom: 2px; }
    .sub-title { font-size: 14px; color: #888; margin-bottom: 20px; }
    .metric-box { background-color: #1e222d; padding: 15px; border-radius: 8px; border: 1px solid #2a2e39; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📈 S&P 500 Custom Indicator Stock Screener</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Combined Net-Volume + Mean-Reversion Histogram Screener</div>', unsafe_allow_html=True)

# Sidebar Controls
st.sidebar.header("🎯 Screening Settings")

min_green = st.sidebar.slider(
    "Minimum Green Bar Value",
    min_value=0.1,
    max_value=9.0,
    value=1.0,
    step=0.1,
    help="Filters stocks where the current green bar depth/magnitude >= this value."
)

all_sectors = ["All"] + sorted(list(set(s["sector"] for s in SP500_COMPONENTS)))
selected_sector = st.sidebar.selectbox("Filter by Sector", all_sectors)

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

# Main Action Button
start_scan = st.button("⚡ START S&P 500 SCREENING", type="primary", use_container_width=True)

if "results" not in st.session_state:
    st.session_state["results"] = None

if start_scan:
    stocks = SP500_COMPONENTS if selected_sector == "All" else [s for s in SP500_COMPONENTS if s["sector"] == selected_sector]
    total_stocks = len(stocks)
    
    progress_bar = st.progress(0, text=f"Starting scan across {total_stocks} S&P 500 stocks...")
    status_text = st.empty()
    
    results = []
    start_time = time.time()
    
    def process_stock(stock_meta):
        symbol = stock_meta["symbol"]
        df = get_stock_data(symbol)
        if df is not None and len(df) >= 30:
            m = get_latest_metrics(
                df, symbol=symbol, min_threshold=min_green,
                w1=w1, w2=w2, nv_length=nv_len, norm_len=norm_len, oversold_level=oversold_lvl
            )
            if m:
                m["name"] = stock_meta["name"]
                m["sector"] = stock_meta["sector"]
                m["industry"] = stock_meta["industry"]
                return m
        return None

    scanned = 0
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_stock = {executor.submit(process_stock, s): s for s in stocks}
        for future in as_completed(future_to_stock):
            scanned += 1
            stk = future_to_stock[future]
            progress = scanned / total_stocks
            progress_bar.progress(progress, text=f"Scanning ({scanned}/{total_stocks}): Analyzing {stk['symbol']}...")
            
            res = future.result()
            if res and res["green_bar_value"] >= min_green:
                results.append(res)
                
    elapsed = round(time.time() - start_time, 1)
    progress_bar.empty()
    status_text.success(f"✅ Screening completed in {elapsed}s! Found {len(results)} matching stocks out of {scanned} scanned.")
    
    results.sort(key=lambda x: x["green_bar_value"], reverse=True)
    st.session_state["results"] = results

# Display Results if available
if st.session_state["results"] is not None:
    res = st.session_state["results"]
    
    # Filter by Signal if requested
    if signal_filter == "🟠 Early Buy Signal Only":
        res = [r for r in res if r["early_buy_signal"]]
    elif signal_filter == "🟡 Confirmed Buy Signal Only":
        res = [r for r in res if r["confirmed_buy_signal"]]
        
    # Summary Metrics Row
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Qualified Stocks", len(res))
    with c2:
        top_val = res[0]["green_bar_value"] if len(res) > 0 else 0.0
        st.metric("Highest Green Bar Depth", f"{top_val:.2f} / 10.0")
    with c3:
        early_cnt = sum(1 for r in res if r["early_buy_signal"])
        st.metric("Early Buy Signals (🟠)", early_cnt)
    with c4:
        conf_cnt = sum(1 for r in res if r["confirmed_buy_signal"])
        st.metric("Confirmed Buy Signals (🟡)", conf_cnt)
        
    st.markdown("### 📋 Qualified Stocks Table")
    
    if len(res) > 0:
        table_data = []
        for r in res:
            table_data.append({
                "Ticker": r["symbol"],
                "Company Name": r["name"],
                "Sector": r["sector"],
                "Price ($)": f"${r['close']:.2f}",
                "24h Change (%)": f"{r['change_pct']:+.2f}%",
                "Green Bar Value (0-10)": r["green_bar_value"],
                "Rating": r["rating"],
                "Net Vol Comp": r["norm1"],
                "Mean Rev Comp": r["norm2"],
                "Composite Osc": r["composite"],
                "Early Buy": "🟠 YES" if r["early_buy_signal"] else "—",
                "Confirmed Buy": "🟡 YES" if r["confirmed_buy_signal"] else "—"
            })
            
        df_table = pd.DataFrame(table_data)
        st.dataframe(df_table, use_container_width=True, height=450)
        
        # Download Button
        csv_data = df_table.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv_data,
            file_name="sp500_green_bar_screener_results.csv",
            mime="text/csv"
        )
        
        # Interactive Stock Inspector & Chart
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
                st.markdown(f"Price: **${selected_stock['close']}** ({selected_stock['change_pct']:+.2f}%) | Sector: **{selected_stock['sector']}**")
            with c_right:
                st.markdown(f"Green Bar Depth: **{selected_stock['green_bar_value']:.2f} / 10.0** ({selected_stock['rating']})")
                
            st.line_chart(df_hist[["close"]], use_container_width=True)
            st.markdown("**Combined Green Bar Histogram (Lower Pane Magnitude 0–10):**")
            st.bar_chart(df_hist[["combined"]].abs(), use_container_width=True)
    else:
        st.info("No stocks match the current filter. Try lowering the minimum green bar threshold.")
else:
    st.info("👋 Welcome! Click the **'START S&P 500 SCREENING'** button above to begin scanning all 500 US S&P 500 stocks.")
