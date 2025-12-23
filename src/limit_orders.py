import sys
import logging
from config import get_client
from utils import validate_side, validate_quantity, validate_price
from logger import setup_logger

setup_logger()

def place_limit_order(api_key, api_secret, symbol, side, quantity, price):
    validate_side(side)
    validate_quantity(quantity)
    validate_price(price)

    client = get_client(api_key, api_secret)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logging.info(f"Limit Order Placed: {order}")
    print(order)

if __name__ == "__main__":
    _, api_key, api_secret, symbol, side, quantity, price = sys.argv
    place_limit_order(api_key, api_secret, symbol, side, float(quantity), float(price))
