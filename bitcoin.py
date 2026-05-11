import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin", "vs_currencies": "usd"}
valasz = requests.get(url, params=params)
ar = valasz.json()["bitcoin"]["usd"]
print(f"Bitcoin ára: ${ar:,.0f}")