import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(data, title='Performance Heatmap', xlabel='Strategies', ylabel='Market Conditions'):
    """
    Plots a heatmap for the given performance data.

    Parameters:
    - data: DataFrame containing performance metrics with strategies as columns and market conditions as index.
    - title: Title of the heatmap.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def create_performance_heatmap(metrics_df):
    """
    Creates a heatmap from the performance metrics DataFrame.

    Parameters:
    - metrics_df: DataFrame with strategies as columns and market conditions as index.
    """
    plot_heatmap(metrics_df)