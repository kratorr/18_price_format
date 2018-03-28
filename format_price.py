import sys


def format_price(price):
    try:
        if (type(price) != int and type(price) != str and type(price) != float):
            return None
        price = round(float(price), 2)
        if str(price).endswith(".0") or str(price).endswith(".00"):
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
