from aemet_metereologico import racha

tickers = ["DIS", "KO", "PEP", "INTC", "F", "V"]

for t in tickers:
    cliente(ticker=t, verbose=True)