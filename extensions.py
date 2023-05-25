import requests
import json

currency={
    'доллар':'USD',
    'евро':'EUR',
    'рубль':'RUB'
}

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote:str,base:str,amount:str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        quote_ticker, base_ticker = currency[quote], currency[base]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "G2fpfcxg4EuR1KMB9AkeyjbLpIOPZzcn"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.text
        return result[result.index("resu")+9:len(result)-3]