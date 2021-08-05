import requests

class CurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, fromCurrency, toCurrency, amount):
        if fromCurrency != 'USD':
            amount = amount / self.currencies[fromCurrency]

        amount = round(amount * self.currencies[toCurrency], 4)
        return amount

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
print(converter.convert("EUR", "USD", 1))