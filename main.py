from aemet_metereologico import racha

tickers = ["5530E", "5514", "5047E", "5051X", "5582A", "6268X"]

for t in tickers:
    racha(ticker=t, verbose=True)