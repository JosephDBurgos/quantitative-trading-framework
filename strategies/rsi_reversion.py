class RSIReversionStrategy(StrategyBase):
    def __init__(self, ticker, period=14, overbought=70, oversold=30):
        super().__init__(ticker)
        self.period = period
        self.overbought = overbought
        self.oversold = oversold

    def generate_signals(self, data):
        rsi = self.calculate_rsi(data['Close'], self.period)
        signals = pd.Series(index=data.index)

        signals[rsi < self.oversold] = 1  # Buy signal
        signals[rsi > self.overbought] = -1  # Sell signal
        signals.fillna(0, inplace=True)  # No position
        return signals

    def backtest(self, data):
        signals = self.generate_signals(data)
        returns = data['Close'].pct_change().shift(-1)  # Shift to align with signals
        strategy_returns = signals * returns
        return strategy_returns.cumsum()  # Cumulative returns

    @staticmethod
    def calculate_rsi(prices, period):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi