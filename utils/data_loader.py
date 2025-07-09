import pandas as pd
import os

def load_asset_data(asset, interval_name):
    filename = os.path.join("../data", f"{asset}_{interval_name}.csv")
    return pd.read_csv(filename, index_col=0, parse_dates=True)