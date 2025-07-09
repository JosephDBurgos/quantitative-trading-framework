class BacktestEngine:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data
        self.results = None

    def run_backtest(self):
        self.data['signals'] = self.strategy.generate_signals(self.data)
        self.data['returns'] = self.data['signals'].shift(1) * self.data['close'].pct_change()
        self.results = self.data['returns'].cumsum()

    def get_results(self):
        return self.results

    def reset(self):
        self.results = None
        self.data['signals'] = None
        self.data['returns'] = None