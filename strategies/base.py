class StrategyBase:
    def generate_signals(self, data):
        """
        Generate trading signals based on the provided data.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def backtest(self, data):
        """
        Backtest the strategy using the provided historical data.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")