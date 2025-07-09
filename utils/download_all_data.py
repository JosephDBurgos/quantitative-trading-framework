import yfinance as yf
import os
from assets_config import ASSETS, INTERVALS

os.makedirs("../data", exist_ok=True)

for asset in ASSETS:
    for interval_name, start, end in INTERVALS:
        filename = f"../data/{asset}_{interval_name}.csv"
        if not os.path.exists(filename):
            df = yf.download(asset, start=start, end=end, auto_adjust=True)
            if not df.empty:
                df[['Close']].to_csv(filename)
                print(f"Saved {filename}")
            else:
                print(f"No data for {asset} in {interval_name}")