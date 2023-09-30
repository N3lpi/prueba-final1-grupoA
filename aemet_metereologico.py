import requests
from mongodb import client


def racha(ticker: str, verbose: bool = False) -> dict:
    url = f"https://opendata.aemet.es/opendata/sh/93cc5cfb{ticker}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()

    nombre = r['chart']['result'][0]['meta']['regularMarketPrice']
    dir = r['chart']['result'][0]['meta']['currency']

    if verbose:
        print(f"{ticker}: {nombre} {dir}")
    return {
        "ticker": ticker,
        "presMin": nombre,
        "presMax": dir
    }


def racha(document: dict):
    _ = client.get_database('tickers').get_collection('metereo').insert_one(document=document)
    return 'ok'