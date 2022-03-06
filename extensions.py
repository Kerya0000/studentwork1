import requests
import json
from config import *

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException("Вы хотите перевести одинаковую валюту. Так делать нельзя.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Я не смог обработать валюту {quote} :(")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Я не смог обработать валюту {base} :(")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Я не смог обработать количество {amount} :(")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]

        return total_base
