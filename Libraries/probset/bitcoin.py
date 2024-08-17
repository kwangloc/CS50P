import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            number_of_btc = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            dollar_convert = number_of_btc*get_bitcoin_price()
            print(f"${dollar_convert:,.4f}", end="")

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        return o["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit()

main()