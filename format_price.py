import sys


def format_price(price):
    try:
        price = round(float(price), 2)
    except ValueError:
        return None
    if price.is_integer():
        return "{:,.0f}".format(price).replace(',', ' ')
    else:
        return "{:,.2f}".format(price).replace(',', ' ')


if __name__ == "__main__":
    try:
        price = sys.argv[1]
        print(format_price(price))
    except IndexError:
        print("Price not found")
