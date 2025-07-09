# Quantitative Strategy Backtester and Evaluator

This project is a comprehensive framework for evaluating multiple trading strategies across various market regimes, timeframes, and asset classes. It is designed to be modular, extensible, and production-aware, showcasing practical quantitative research, backtesting, and analytics.

## Project Structure

- **data/**: Contains raw downloaded data or cached results.
- **strategies/**: Implements trading strategies.
  - **base.py**: Defines the `StrategyBase` class with a common interface for all strategies.
  - **moving_average.py**: Implements the moving average crossover strategy.
  - **rsi_reversion.py**: Implements the RSI-based mean reversion strategy.
- **backtest/**: Contains the backtesting engine and performance metrics.
  - **engine.py**: Runs simulations of trading strategies on historical data.
  - **metrics.py**: Computes key performance metrics such as Sharpe ratio and max drawdown.
- **analysis/**: Provides visualization tools for analyzing strategy performance.
  - **plots.py**: Generates visualizations like equity curves and drawdown plots.
  - **heatmaps.py**: Creates heatmaps for comparing performance metrics.
- **notebooks/**: Contains Jupyter notebooks for exploratory analysis.
  - **experiments.ipynb**: Used for interactive testing and visualization of strategies.
- **reports/**: Stores exported PDF writeups or summaries of project findings.
  - **summary.pdf**: Contains performance metrics and visualizations.
- **app/**: (Optional) Contains the Streamlit app or dashboard for visualizing results.
  - **dashboard.py**: Visualizes the results of backtests and allows user interaction.
- **README.md**: Documentation for the project, including setup instructions and usage.
- **requirements.txt**: Lists dependencies required for the project.
- **main.py**: Entry point to run batch experiments and orchestrate strategy execution.

## Project Goals

- Implement multiple trading strategies with a common interface.
- Evaluate performance across different tickers, time periods, and market regimes.
- Generate visual reports that clearly communicate findings.
- Build reusable tools for strategy testing, signal generation, and risk evaluation.
- Demonstrate knowledge in financial engineering, Python programming, data science, statistics, and trading systems design.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd quant_project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the main script to execute batch experiments:
   ```
   python main.py
   ```

## Usage

- Modify the strategy classes in the `strategies/` directory to implement your own trading logic.
- Use the Jupyter notebook in `notebooks/` for exploratory analysis and testing.
- Visualize results using the functions in the `analysis/` directory or the optional dashboard in `app/`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.