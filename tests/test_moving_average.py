import pandas as pd
import pytest
import yfinance as yf
from strategies.moving_average import MovingAverageStrategy

@pytest.mark.integration
def test_generate_signals_with_real_data():
    # Download real historical data for AAPL
    data = yf.download("AAPL", start="2024-01-01", end="2024-03-01", auto_adjust=True)
    assert not data.empty, "Downloaded data is empty"

    # Use only the 'Close' column as expected by the strategy
    data = data[['Close']]

    # Instantiate and generate signals
    strategy = MovingAverageStrategy(data, short_window=5, long_window=20)
    signals = strategy.generate_signals()

    # Basic checks (no saving files)
    assert isinstance(signals, pd.DataFrame)
    assert 'signal' in signals.columns
    assert 'short_mavg' in signals.columns
    assert 'long_mavg' in signals.columns
    assert 'positions' in signals.columns
    assert len(signals) == len(data)