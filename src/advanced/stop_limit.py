import sys
import logging
from config import get_client
from utils import validate_side, validate_quantity, validate_price
from logger import setup_logger

setup_logger()

def place_stop_limit(api_key, api_secret, symbol, side, quantity, stop_price, limit_price):
    validate_side(side)
    validate_quantity(quantity)
    validate_price(stop_price)
    validate_price(limit_price)

    client = get_client(api_key, api_secret)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="STOP",
        quantity=quantity,
        stopPrice=stop_price,
        price=limit_price,
        timeInForce="GTC"
    )

    logging.info(f"Stop-Limit Order Placed: {order}")
    print(order)

if __name__ == "__main__":
    _, api_key, api_secret, symbol, side, quantity, stop_price, limit_price = sys.argv
    place_stop_limit(
        api_key, api_secret, symbol, side,
        float(quantity), float(stop_price), float(limit_price)
    )
