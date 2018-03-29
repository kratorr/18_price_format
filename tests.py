from format_price import format_price
import unittest


class PriceFormatTestCase(unittest.TestCase):
    def test_int_format(self):
        price = format_price(666666)
        self.assertEqual(price, "666 666")

    def test_string_numbers_int(self):
        price = format_price("123456")
        self.assertEqual(price, "123 456")

    def test_string_numbers_float(self):
        price = format_price("123456.37")
        self.assertEqual(price, "123 456.37")

    def test_float_zero_frac(self):
        price = format_price(123456.0)
        self.assertEqual(price, "123 456")

    def test_string_numbers_float_zero_frac(self):
        price = format_price("3245.000000")
        self.assertEqual(price, "3 245")

    def test_string_numbers_float_non_zero_frac(self):
        price = format_price("3245.000001")
        self.assertEqual(price, "3 245")

    def test_string_not_digit(self):
        price = format_price("144y.e.")
        self.assertIsNone(price)

    def test_empty_string(self):
        price = format_price("")
        self.assertIsNone(price)

    def test_bool(self):
        price = format_price(True)
        self.assertIsNone(None)

    def test_zero_int(self):
        price = format_price(0)
        self.assertEqual(price, "0")



if __name__ == '__main__':
    unittest.main()
