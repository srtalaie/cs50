import sys

import requests

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

obj = r.json()
price = obj["bpi"]["USD"]["rate_float"]

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif type(float(sys.argv[1])) == float:
        coins = float(sys.argv[1])
        amount = coins * price
        print(f"${amount:,.4f}")
    else:
        sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit()
