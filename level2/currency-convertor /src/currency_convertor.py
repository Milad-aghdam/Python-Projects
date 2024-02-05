# Import the requests library
import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3*60*60)

# Define a function to convert one currency to another
@cached(cache)
def convert_currency(from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    if response.status_code != 200:
        return None
    return response.json()['rates'][to_currency]

# Define a function to calculate the amount in the target currency
def calculate_amount(exchange_rate, base_amount):
    return exchange_rate * base_amount

if __name__ == '__main__':
    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = float(input("Enter amount: "))
    exchange_rate = convert_currency(base_currency, target_currency)
    converted_amount = calculate_amount(amount, exchange_rate)
    print(f"{amount} {base_currency} is {converted_amount} {target_currency}")