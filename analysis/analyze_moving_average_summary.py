import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def analyze_moving_average_summary():
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
    STRATEGY_DIR = os.path.join(RESULTS_DIR, "moving_average")
    os.makedirs(STRATEGY_DIR, exist_ok=True)
    SUMMARY_FILE = os.path.join(STRATEGY_DIR, "moving_average_summary.csv")

    # Load summary
    df = pd.read_csv(SUMMARY_FILE)

    # Pivot for heatmap (assets x intervals, values = total_return)
    pivot = df.pivot(index="asset", columns="interval", values="total_return")

    # Show basic stats
    print("Top 10 assets by average return:")
    print(pivot.mean(axis=1).sort_values(ascending=False).head(10))

    print("\nTop 10 intervals by average return:")
    print(pivot.mean(axis=0).sort_values(ascending=False).head(10))

    # --- Improved Heatmap: Show only top N assets for readability ---
    TOP_N_ASSETS = 30  # Change as needed
    top_assets = pivot.mean(axis=1).sort_values(ascending=False).head(TOP_N_ASSETS).index
    pivot_top = pivot.loc[top_assets]

    plt.figure(figsize=(min(2 + len(pivot_top.columns), 18), 1 + 0.5 * len(pivot_top)))
    sns.set_theme(font_scale=1.2)
    mask = pivot_top.isnull()

    # Calculate robust vmin/vmax for color scaling (ignore extreme outliers)
    all_returns = pivot_top.values.flatten()
    all_returns = all_returns[~pd.isnull(all_returns)]
    vmin = np.percentile(all_returns, 1)
    vmax = np.percentile(all_returns, 99)

    ax = sns.heatmap(
        pivot_top,
        annot=False,
        cmap="RdYlGn",
        center=0,
        linewidths=1,
        linecolor='black',
        mask=mask,
        cbar_kws={'label': 'Total Return (%)'},
        square=False,
        vmin=vmin,
        vmax=vmax
    )

    ax.set_yticks(range(len(pivot_top.index)))
    ax.set_yticklabels(pivot_top.index, fontsize=12, fontweight='bold')
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=10)
    ax.set_facecolor('lightgray')

    plt.title(f"Moving Average Strategy: Total Return (%) by Asset and Interval (Top {TOP_N_ASSETS} Assets)", fontsize=16, pad=20, fontweight='bold')
    plt.xlabel("Interval", fontsize=12, fontweight='bold')
    plt.ylabel("Asset", fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(STRATEGY_DIR, "moving_average_heatmap.png"))
    plt.show()

    # --- Improved Return Distribution ---
    plt.figure(figsize=(8, 5))
    returns = pivot.stack()  # Do NOT multiply by 100
    plt.hist(returns, bins=50, color='skyblue', edgecolor='black')
    plt.title("Distribution of Total Returns (All Assets & Intervals)", fontsize=14, fontweight='bold')
    plt.xlabel("Total Return (%)", fontsize=12, fontweight='bold')
    plt.ylabel("Frequency", fontsize=12, fontweight='bold')
    plt.xlim(returns.min() - 5, returns.max() + 5)
    plt.tight_layout()
    plt.savefig(os.path.join(STRATEGY_DIR, "moving_average_return_distribution.png"))
    plt.show()

    # --- Bar plot for each interval with robust y-axis scaling ---
    intervals = pivot.columns.tolist()
    for interval in intervals:
        data = pivot[interval].dropna().sort_values(ascending=False)  # Do NOT multiply by 100
        num_assets = len(data)
        fig_width = min(max(12, num_assets * 0.4), 24)
        font_size = 10 if num_assets < 30 else 8 if num_assets < 60 else 6

        # Robust y-axis scaling: ignore extreme outliers
        y_min = np.percentile(data.values, 1)
        y_max = np.percentile(data.values, 99)

        plt.figure(figsize=(fig_width, 6))
        plt.bar(data.index, data.values, color='green')
        plt.title(f"Total Return (%) by Asset for Interval: {interval}", fontsize=16, fontweight='bold')
        plt.xlabel("Asset", fontsize=12, fontweight='bold')
        plt.ylabel("Total Return (%)", fontsize=12, fontweight='bold')
        plt.xticks(
            ticks=range(num_assets),
            labels=data.index,
            rotation=90,
            fontsize=font_size,
            fontweight='bold'
        )
        plt.ylim(y_min, y_max)
        plt.tight_layout()
        plt.savefig(os.path.join(STRATEGY_DIR, f"bar_{interval}.png"))
        plt.close()