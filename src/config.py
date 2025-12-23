from binance.client import Client

TESTNET_FUTURES_URL = "https://testnet.binancefuture.com"

def get_client(api_key, api_secret):
    client = Client(api_key, api_secret)

    # Explicitly override Futures REST endpoint
    client.FUTURES_URL = TESTNET_FUTURES_URL

    return client
