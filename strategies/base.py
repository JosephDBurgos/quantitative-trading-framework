from abc import ABC, abstractmethod

class StrategyBase(ABC):
    def __init__(self, data):
        self.data = data
        self.signals = None

    @abstractmethod
    def generate_signals(self):
        pass

    def backtest(self):
        # Later: optionally implement basic backtest logic here
        pass