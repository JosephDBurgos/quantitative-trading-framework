import os
import pandas as pd
from utils.assets_config import ASSETS, INTERVALS
from utils.data_loader import load_asset_data
from strategies.moving_average import MovingAverageStrategy

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")

results = []

for asset in ASSETS:
    for interval_name, _, _ in INTERVALS:
        filename = os.path.join(DATA_DIR, f"{asset}_{interval_name}.csv")
        if not os.path.exists(filename):
            print(f"Skipping {asset} {interval_name}: file does not exist.")
            continue
        try:
            # Try to skip extra header rows if present
            with open(filename, "r") as f:
                first_line = f.readline().strip()
            if first_line.lower() in ["price,close", "date,close"]:
                # File has extra headers, skip first 3 rows
                data = pd.read_csv(
                    filename,
                    skiprows=3,
                    index_col=0,
                    parse_dates=True,
                    names=["Date", "Close"]
                )
            else:
                # Standard format
                data = pd.read_csv(
                    filename,
                    index_col=0,
                    parse_dates=True
                )
            if data.empty or 'Close' not in data.columns or not pd.api.types.is_numeric_dtype(data['Close']):
                print(f"Skipping {asset} {interval_name}: 'Close' column missing or not numeric.")
                continue
            strategy = MovingAverageStrategy(data)
            signals = strategy.generate_signals()
            total_return = (data['Close'].iloc[-1] / data['Close'].iloc[0]) - 1
            num_trades = signals['positions'].abs().sum()
            results.append({
                "asset": asset,
                "interval": interval_name,
                "total_return": total_return,
                "num_trades": num_trades,
            })
        except Exception as e:
            print(f"Error processing {asset} {interval_name}: {e}")

# Save summary
os.makedirs(RESULTS_DIR, exist_ok=True)
df_results = pd.DataFrame(results)
df_results.to_csv(os.path.join(RESULTS_DIR, "moving_average_summary.csv"), index=False)

if not df_results.empty:
    pivot = df_results.pivot(index="asset", columns="interval", values="total_return")
    print(pivot)
else:
    print("No results to display. Check if your data files exist and contain data.")