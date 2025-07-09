from matplotlib import pyplot as plt
import pandas as pd

def plot_equity_curve(equity_curve: pd.Series, title: str = "Equity Curve"):
    plt.figure(figsize=(12, 6))
    plt.plot(equity_curve.index, equity_curve.values, label='Equity', color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Equity Value')
    plt.legend()
    plt.grid()
    plt.show()

def plot_drawdown(drawdown: pd.Series, title: str = "Drawdown Plot"):
    plt.figure(figsize=(12, 6))
    plt.fill_between(drawdown.index, drawdown.values, color='red', alpha=0.5)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Drawdown')
    plt.grid()
    plt.show()

def plot_parameter_heatmap(data: pd.DataFrame, title: str = "Parameter Heatmap"):
    plt.figure(figsize=(10, 8))
    heatmap = plt.pcolor(data, cmap=plt.cm.RdYlGn)
    plt.colorbar(heatmap)
    plt.title(title)
    plt.xlabel('Parameters')
    plt.ylabel('Metrics')
    plt.xticks(ticks=range(len(data.columns)), labels=data.columns)
    plt.yticks(ticks=range(len(data.index)), labels=data.index)
    plt.show()