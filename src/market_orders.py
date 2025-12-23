import sys
import logging
from config import get_client
from utils import validate_side, validate_quantity
from logger import setup_logger

setup_logger()

def place_market_order(api_key, api_secret, symbol, side, quantity):
    validate_side(side)
    validate_quantity(quantity)

    client = get_client(api_key, api_secret)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(f"Market Order Executed: {order}")
    print(order)

if __name__ == "__main__":
    _, api_key, api_secret, symbol, side, quantity = sys.argv
    place_market_order(api_key, api_secret, symbol, side, float(quantity))
