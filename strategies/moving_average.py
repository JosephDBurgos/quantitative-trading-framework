import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from strategies.base import StrategyBase

class MovingAverageStrategy(StrategyBase):
    def __init__(self, data, short_window=50, long_window=200):
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window
        self.signals = None

    def generate_signals(self):
        data = self.data
        short_mavg = data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        long_mavg = data['Close'].rolling(window=self.long_window, min_periods=1).mean()

        signals = pd.DataFrame(index=data.index)
        signals['short_mavg'] = short_mavg
        signals['long_mavg'] = long_mavg

        # 1.0 when short > long, 0.0 otherwise (in or out of market)
        signals['signal'] = np.where(signals['short_mavg'] > signals['long_mavg'], 1.0, 0.0)
        # Entry/exit points: 1.0 = buy, -1.0 = sell
        signals['positions'] = signals['signal'].diff().fillna(0.0)

        self.signals = signals
        return signals

    def save_signals(self, filename="results/moving_average_signals.csv"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if self.signals is not None:
            self.signals.to_csv(filename)
        else:
            raise ValueError("No signals to save. Run generate_signals() first.")

    def save_plot(self, filename="results/moving_average_signals.png"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if self.signals is None:
            self.generate_signals()
        signals = self.signals
        data = self.data

        plt.figure(figsize=(14, 7))
        plt.plot(data.index, data['Close'], label='Close Price', color='black', alpha=0.5)
        plt.plot(signals.index, signals['short_mavg'], label=f'Short MA ({self.short_window})', color='blue')
        plt.plot(signals.index, signals['long_mavg'], label=f'Long MA ({self.long_window})', color='red')

        buy_signals = signals[signals['positions'] == 1.0]
        plt.scatter(buy_signals.index, data.loc[buy_signals.index, 'Close'], marker='^', color='green', label='Buy Signal', s=100)

        sell_signals = signals[signals['positions'] == -1.0]
        plt.scatter(sell_signals.index, data.loc[sell_signals.index, 'Close'], marker='v', color='red', label='Sell Signal', s=100)

        plt.title('Moving Average Strategy Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    def backtest(self):
        signals = self.generate_signals()
        # Implement backtesting logic here
        return signals
