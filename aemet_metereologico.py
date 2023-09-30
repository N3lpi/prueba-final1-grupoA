import os
import requests
from mongodb import client
from dotenv import load_dotenv

def racha(ticker: str) -> dict:
    api_key = os.getenv('API_KEY')
    url = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/normales/estacion/{ticker}/?api_key={api_key}"
    r = requests.get(url).json()

    dato = r['datos']

    a=requests.get(dato).json()

    indi = a['indicativo']
    tor = a['n_tor_n']
    mx = a['q_max_n']




