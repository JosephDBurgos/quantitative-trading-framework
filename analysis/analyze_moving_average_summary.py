import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
SUMMARY_FILE = os.path.join(RESULTS_DIR, "moving_average_summary.csv")

# Load summary
df = pd.read_csv(SUMMARY_FILE)

# Pivot for heatmap (assets x intervals, values = total_return)
pivot = df.pivot(index="asset", columns="interval", values="total_return")

# Show basic stats
print("Top 10 assets by average return:")
print(pivot.mean(axis=1).sort_values(ascending=False).head(10))

print("\nTop 10 intervals by average return:")
print(pivot.mean(axis=0).sort_values(ascending=False).head(10))

# Plot heatmap of total returns
plt.figure(figsize=(16, 10))
sns.heatmap(pivot, annot=False, cmap="RdYlGn", center=0)
plt.title("Moving Average Strategy: Total Return by Asset and Interval")
plt.xlabel("Interval")
plt.ylabel("Asset")
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, "moving_average_heatmap.png"))
plt.show()

# Optional: plot distribution of returns
plt.figure(figsize=(8, 5))
pivot.stack().hist(bins=50)
plt.title("Distribution of Total Returns (All Assets & Intervals)")
plt.xlabel("Total Return")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, "moving_average_return_distribution.png"))
plt.show()