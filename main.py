import pandas as pd
from strategies.base import StrategyBase
from backtest.engine import BacktestEngine
from analysis.plots import plot_equity_curve
from analysis.heatmaps import create_heatmap

def main():
    # Define the tickers, date range, and strategies to test
    tickers = ['SPY', 'QQQ', 'TSLA']
    date_range = ('2012-01-01', '2024-01-01')
    
    # Initialize the backtest engine
    backtest_engine = BacktestEngine()

    # List to store results
    results = []

    # Loop through each strategy
    strategies = [MovingAverageStrategy(), RSIReversionStrategy()]
    for strategy in strategies:
        for ticker in tickers:
            # Run backtest for each ticker
            performance = backtest_engine.run_backtest(strategy, ticker, date_range)
            results.append(performance)

    # Convert results to DataFrame for analysis
    results_df = pd.DataFrame(results)

    # Generate visualizations
    for result in results_df.itertuples():
        plot_equity_curve(result)

    # Create heatmap for performance comparison
    create_heatmap(results_df)

if __name__ == "__main__":
    main()