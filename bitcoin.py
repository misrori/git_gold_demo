import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin", "vs_currencies": "usd"}
valasz = requests.get(url, params=params)
ar = valasz.json()["bitcoin"]["usd"]
print(f"Bitcoin ára: ${ar:,.0f}")


import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
valasz = requests.get(url, params=params)
adat = valasz.json()
print(f"Bitcoin:  ${adat['bitcoin']['usd']:,.0f}")
print(f"Ethereum: ${adat['ethereum']['usd']:,.0f}")
