class MovingAverageStrategy(StrategyBase):
    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window
        self.signals = None

    def generate_signals(self, data):
        """Generate trading signals based on moving average crossover."""
        short_mavg = data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        long_mavg = data['Close'].rolling(window=self.long_window, min_periods=1).mean()

        signals = pd.DataFrame(index=data.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = short_mavg
        signals['long_mavg'] = long_mavg

        signals['signal'][self.short_window:] = np.where(
            signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0
        )
        signals['positions'] = signals['signal'].diff()

        self.signals = signals
        return signals

    def backtest(self, data):
        """Backtest the strategy and return performance metrics."""
        signals = self.generate_signals(data)
        # Implement backtesting logic here (e.g., calculating returns based on signals)
        # This is a placeholder for the actual backtesting implementation
        return signals