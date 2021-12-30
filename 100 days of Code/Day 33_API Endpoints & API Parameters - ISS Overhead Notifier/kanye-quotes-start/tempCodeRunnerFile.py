import requests
from requests.api import get

def get_quote():
    quote = requests.get(url="https://api.kanye.rest/")
    quote = quote.json()
    print(quote)
get_quote()