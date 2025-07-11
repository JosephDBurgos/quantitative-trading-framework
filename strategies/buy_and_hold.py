import os
import pandas as pd
import matplotlib.pyplot as plt
from strategies.base import StrategyBase

class BuyAndHoldStrategy(StrategyBase):
    def __init__(self, data):
        super().__init__(data)
        self.signals = None

    def generate_signals(self):
        data = self.data
        signals = pd.DataFrame(index=data.index)
        signals['signal'] = 1.0  # Always in the market
        signals['positions'] = signals['signal'].diff().fillna(1.0)  # Buy at the start
        self.signals = signals
        return signals

    def save_signals(self, filename="results/buy_and_hold_signals.csv"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if self.signals is not None:
            self.signals.to_csv(filename)
        else:
            raise ValueError("No signals to save. Run generate_signals() first.")

    def save_plot(self, filename="results/buy_and_hold_signals.png"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if self.signals is None:
            self.generate_signals()
        signals = self.signals
        data = self.data

        plt.figure(figsize=(14, 7))
        plt.plot(data.index, data['Close'], label='Close Price', color='black', alpha=0.5)
        buy_signals = signals[signals['positions'] == 1.0]
        plt.scatter(buy_signals.index, data.loc[buy_signals.index, 'Close'], marker='^', color='green', label='Buy Signal', s=100)
        plt.title('Buy and Hold Strategy Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    def backtest(self):
        signals = self.generate_signals()
        # Implement backtesting logic here if needed
        return signals
