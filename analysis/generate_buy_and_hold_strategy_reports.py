import os
import pandas as pd
from utils.assets_config import ASSETS, INTERVALS
from utils.data_loader import load_asset_data
from strategies.buy_and_hold import BuyAndHoldStrategy

def generate_buy_and_hold_reports():
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(PROJECT_ROOT, "data")
    RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
    STRATEGY_DIR = os.path.join(RESULTS_DIR, "buy_and_hold")
    os.makedirs(STRATEGY_DIR, exist_ok=True)

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
                strategy = BuyAndHoldStrategy(data)
                signals = strategy.generate_signals()
                signals['daily_returns'] = data['Close'].pct_change()
                total_return = (1 + signals['daily_returns']).prod() - 1
                num_trades = 1  # Buy and hold: only one trade
                results.append({
                    "asset": asset,
                    "interval": interval_name,
                    "total_return": total_return,
                    "num_trades": num_trades,
                })
            except Exception as e:
                print(f"Error processing {asset} {interval_name}: {e}")

    # Save summary
    df_results = pd.DataFrame(results)
    df_results.to_csv(os.path.join(STRATEGY_DIR, "buy_and_hold_summary.csv"), index=False)

    if not df_results.empty:
        pivot = df_results.pivot(index="asset", columns="interval", values="total_return")
        print(pivot)
    else:
        print("No results to display. Check if your data files exist and contain data.")
