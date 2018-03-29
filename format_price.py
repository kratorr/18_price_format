import sys
import math


def format_price(price):
    min_fraction = 0.01
    try:
        price = round(float(price), 2)
        fraction, _ = math.modf(price)
        if fraction < min_fraction:
            return "{:,.0f}".format(price).replace(',', ' ')
        elif str(price).endswith("0"):
            return "{:,.1f}".format(price).replace(',', ' ')
        else:
            return "{:,.2f}".format(price).replace(',', ' ')
    except ValueError:
        return None


if __name__ == "__main__":
    try:
        price = sys.argv[1]
        print(format_price(price))
    except IndexError:
        print("Price not found")
