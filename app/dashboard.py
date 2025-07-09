import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from backtest.metrics import compute_metrics
from analysis.plots import plot_equity_curve

# Title of the dashboard
st.title("Quantitative Strategy Backtester Dashboard")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")

# User can select the strategy
strategy_options = ["Moving Average", "RSI Reversion"]
selected_strategy = st.sidebar.selectbox("Select Strategy", strategy_options)

# User can select the ticker
ticker = st.sidebar.text_input("Ticker", "SPY")

# User can select the date range
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2012-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))

# Button to run the backtest
if st.sidebar.button("Run Backtest"):
    # Placeholder for loading data and running the selected strategy
    # This should be replaced with actual data loading and strategy execution
    st.write(f"Running backtest for {selected_strategy} on {ticker} from {start_date} to {end_date}...")
    
    # Example: Load data and run backtest (to be implemented)
    # data = load_data(ticker, start_date, end_date)
    # results = run_strategy(selected_strategy, data)
    
    # Placeholder for results
    results = {
        "equity_curve": [100, 105, 110, 107, 115],  # Example data
        "metrics": compute_metrics([100, 105, 110, 107, 115])  # Example metrics
    }
    
    # Plot equity curve
    st.subheader("Equity Curve")
    plot_equity_curve(results["equity_curve"])
    
    # Display performance metrics
    st.subheader("Performance Metrics")
    st.write(results["metrics"])  # Display computed metrics

# Footer
st.write("Dashboard for visualizing quantitative strategy backtest results.")