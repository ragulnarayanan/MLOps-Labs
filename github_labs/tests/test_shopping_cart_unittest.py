# tests/test_shopping_cart_unittest.py
import unittest
from src.shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 1.0, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["item_name"], "Apple")

    def test_remove_item(self):
        self.cart.add_item("Banana", 0.5, 3)
        self.cart.remove_item("Banana")
        self.assertEqual(len(self.cart.items), 0)

    def test_calculate_total(self):
        self.cart.add_item("Apple", 1.0, 2)
        self.cart.add_item("Banana", 0.5, 3)
        self.assertEqual(self.cart.calculate_total(), 3.5)

    def test_apply_discount(self):
        self.cart.add_item("Apple", 1.0, 2)
        self.cart.add_item("Banana", 0.5, 3)
        self.assertEqual(self.cart.apply_discount(20), 2.8)

    def test_invalid_price_or_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Orange", -1.0, 1)
        with self.assertRaises(ValueError):
            self.cart.add_item("Orange", 1.0, -1)

    def test_invalid_discount(self):
        self.cart.add_item("Apple", 1.0, 2)
        with self.assertRaises(ValueError):
            self.cart.apply_discount(120)

if __name__ == '__main__':
    unittest.main()
