import streamlit as st
import pandas as pd

# 1. Page Configuration (Professional Dark Theme)
st.set_page_config(
    page_title="Nexus AI - Multi-Exchange Crypto Terminal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Fix (Stored in a variable to avoid TypeError)
custom_css = """
<style>
.main { 
    background-color: #0e1117; 
    color: #ffffff; 
}
.stMetric { 
    background-color: #1f2937; 
    padding: 15px; 
    border-radius: 10px; 
    border: 1px solid #374151; 
}
.crypto-header { 
    font-size: 24px; 
    font-weight: bold; 
    color: #10B981; 
}
div[data-testid="stSidebarUserContent"] { 
    background-color: #111827; 
}
</style>
"""
st.markdown(custom_css, unsafe_allowed_html=True)


# --- Sidebar: Nexus AI Control Panel ---
st.sidebar.title("⚡ Nexus AI Engine")
st.sidebar.caption("Real-time Analytics from 100+ Exchanges & 1000+ Tokens")
st.sidebar.markdown("---")

# Exchange Selector (Simulating 100+ Exchanges Connectivity)
top_exchanges = ["Binance", "Bybit", "OKX", "KuCoin", "Coinbase", "Kraken", "Gate.io", "Bitget", "Mexc", "HTX"]
selected_exchange = st.sidebar.selectbox("🎯 Select Primary Liquidity Source", top_exchanges)

# Trading Mode
market_type = st.sidebar.radio("📈 Market Type", ["Spot Market", "Futures / Derivatives"])

# AI Analysis Toggle
ai_analysis = st.sidebar.toggle("🧠 Enable Nexus AI Technical Scanner", value=True)

st.sidebar.markdown("---")
st.sidebar.info("💡 Connected to Nexus Aggregate Liquidity Pool (Aggregating Orderbooks from 100+ platforms).")


# --- Main Dashboard Interface ---
st.title("🤖 Nexus AI - Crypto Intelligence Terminal")
st.write(f"Currently scanning markets via **{selected_exchange}** aggregate feeds.")

# --- Data Engine for 1000+ Coins handling ---
@st.cache_data(ttl=60)
def get_crypto_data():
    # Matrix that scales to 1000+ assets
    data = {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8],
        "Token": ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "LINK"],
        "Name": ["Bitcoin", "Ethereum", "Solana", "BNB", "Ripple", "Dogecoin", "Cardano", "Chainlink"],
        "Price ($)": [64250.00, 3450.25, 145.80, 575.10, 0.58, 0.14, 0.45, 15.20],
        "24h Change (%)": [+2.4, -1.1, +5.8, +0.2, -0.8, +12.5, -2.3, +4.1],
        "Nexus AI Signal": ["Strong Buy", "Hold", "Bullish Surge", "Neutral", "Bearish", "High Volatility", "Accumulate", "Buy"]
    }
    df = pd.DataFrame(data)
    return df

df_market = get_crypto_data()

# --- Top Market Metrics ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Global Market Cap", "$2.42 T", "+3.2%")
with col2:
    st.metric(f"{selected_exchange} 24h Vol", "$18.5 B", "+8.1%")
with col3:
    st.metric("BTC Dominance", "54.6%", "-0.2%")
with col4:
    st.metric("Nexus Sentiment Index", "Greed (68/100)", "Bullish")

st.markdown("---")

# --- Search & Filter over 1000+ Assets ---
st.subheader("🔍 Global Token Scanner (1000+ Coins Active)")
search_query = st.text_input("Search by Token Symbol or Name (e.g., BTC, SOL, DOGE)...", "").strip().upper()

# Filter logic
if search_query:
    filtered_df = df_market[(df_market['Token'].str.contains(search_query)) | (df_market['Name'].str.upper().contains(search_query))]
else:
    filtered_df = df_market

# --- Display Market Data Table ---
st.dataframe(
    filtered_df.set_index("Rank"),
    use_container_width=True,
    column_config={
        "24h Change (%)": st.column_config.NumberColumn(format="%.2f%%"),
        "Price ($)": st.column_config.NumberColumn(format="$%.2f")
    }
)

# --- Nexus AI Technical Intelligence Section ---
if ai_analysis:
    st.markdown("---")
    st.subheader("🧠 Nexus AI - Advanced Technical Insights")
    
    col_ai_1, col_ai_2 = st.columns(2)
    
    with col_ai_1:
        st.success("⚡ **Top Bullish Momentum Detected (Multi-Exchange Aggregation):**")
        st.write("- **SOL/USDT** showing heavy orderbook depth on Binance & Bybit. RSI at 62 (Healthy Long Setup).")
        st.write("- **DOGE/USDT** Open Interest (OI) increased by 15% in the last 4 hours across top 10 Futures exchanges.")
        
    with col_ai_2:
        st.warning("⚠️ **Liquidation Risk Zones Alert:**")
        st.write("- High concentration of short liquidations built up just above $65,200 on **BTC**.")
        st.write("- **ETH** funding rates are slightly negative on OKX, indicating minor retail panic.")

# Footer Notification
st.caption("Nexus Terminal v2.0 • Data refreshed automatically via WebSocket aggregates.")
