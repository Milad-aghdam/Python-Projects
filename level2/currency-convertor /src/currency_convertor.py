# Import the requests library
import requests

# Define a function to convert one currency to another
def convert_currency(from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    if response.status_code != 200:
        return None
    return response.json()['rates'][to_currency]

# Define a function to calculate the amount in the target currency
def calculate_amount(exchange_rate, base_amount):
    return exchange_rate * base_amount