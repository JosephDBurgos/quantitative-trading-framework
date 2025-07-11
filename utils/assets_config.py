ASSETS = [
    # Tech
    "AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "NVDA", "META", "INTC", "ADBE",

    # Banks & Financials
    "JPM", "BAC", "WFC", "GS", "MS", "AXP", "C",

    # Energy
    "XOM", "CVX", "BP", "SLB", "COP",

    # Healthcare
    "JNJ", "PFE", "MRK", "UNH", "LLY", "ABBV",

    # Consumer/Retail
    "HD", "WMT", "TGT", "COST", "MCD", "SBUX",

    # Industrials
    "CAT", "BA", "GE", "MMM", "LMT", "NOC",

    # Utilities
    "DUK", "NEE", "SO", "AEP",

    # Telecom
    "VZ", "T", "TMUS",

    # Materials
    "LIN", "SHW", "APD", "FCX", "NUE",

    # Real Estate
    "PLD", "SPG", "O", "AMT",

    # Transportation
    "UPS", "FDX", "DAL", "UAL",

    # ETFs – Broad Market
    "SPY", "QQQ", "DIA", "IWM", "VTI", "VOO",

    # Sector ETFs
    "XLF", "XLK", "XLV", "XLE", "XLY", "XLI", "XLU", "XLB", "XLRE", "XLC",

    # Bonds
    "TLT", "IEF", "SHY", "LQD", "HYG",

    # Commodities
    "GLD", "SLV", "USO", "DBA",

    # Crypto (optional)
    "BTC-USD", "ETH-USD", "SOL-USD",

    # International / Emerging Markets
    "EWJ", "EEM", "FXI", "EWZ", "INDA", "VEA"
]

INTERVALS = [
    ("1_year",        "2024-06-01", "2025-06-01"),
    ("2_years",       "2023-06-01", "2025-06-01"),
    ("6_months",      "2025-01-01", "2025-06-01"),
    ("3_months",      "2025-03-01", "2025-06-01"),
    ("5_years",       "2020-06-01", "2025-06-01"),
    ("10_years",      "2015-06-01", "2025-06-01"),
    ("15_years",      "2010-06-01", "2025-06-01"),

    # Significant historical regimes
    ("dotcom_bubble", "1999-01-01", "2002-12-31"),
    ("9_11",          "2001-08-01", "2001-12-01"),
    ("2008_crisis",   "2007-07-01", "2009-07-01"),
    ("2011_euro_crisis", "2011-01-01", "2012-01-01"),
    ("2016_election", "2016-06-01", "2017-06-01"),
    ("covid_crash",   "2020-02-01", "2020-06-01"),
    ("covid_bounce",  "2020-06-01", "2021-06-01"),
    ("rate_hike_era", "2022-01-01", "2024-01-01"),
    ("russia_ukraine", "2022-02-01", "2022-12-01"),
]