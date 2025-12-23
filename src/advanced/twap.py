import sys
import time
import logging
from config import get_client
from utils import validate_side, validate_quantity
from logger import setup_logger

setup_logger()

def twap_order(api_key, api_secret, symbol, side, total_qty, parts, interval):
    validate_side(side)
    validate_quantity(total_qty)

    client = get_client(api_key, api_secret)
    qty_per_order = total_qty / parts

    for i in range(parts):
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=round(qty_per_order, 3)
        )

        logging.info(f"TWAP Order {i+1}/{parts}: {order}")
        print(f"Executed part {i+1}")
        time.sleep(interval)

if __name__ == "__main__":
    _, api_key, api_secret, symbol, side, total_qty, parts, interval = sys.argv
    twap_order(
        api_key, api_secret, symbol, side,
        float(total_qty), int(parts), int(interval)
    )
