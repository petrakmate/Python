import requests

def crypto_price(crypto):
    coingecko_url = "https://api.coingecko.com/api/v3/simple/price"
    param = {
        "ids": crypto.lower(),
        "vs_currencies": "usd"
    }
    response = requests.get(coingecko_url, params=param)
    data = response.json()
    price = data[crypto.lower()]["usd"]
    return price

coin_map = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "ADA": "cardano",
    "SOL": "solana",
    "TRX": "tron",
    "DOGE": "dogecoin",
    "XMR": "monero",
    "LINK": "chainlink"
}

crpt_abbrev = input("Which cryptocurrency's price do you want to know? Write the abbreviation here: ").upper()

if crpt_abbrev in coin_map:
    crpt = coin_map[crpt_abbrev]
    crpt_price = crypto_price(crpt)
    print(f"The price of {crpt} is {crpt_price} USD.")
else:
    print("Sorry, this coin is not supported.")
