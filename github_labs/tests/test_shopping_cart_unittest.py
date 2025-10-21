import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        self.cart.add_item("Apple", 1.0, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["name"], "Apple")
        self.assertEqual(self.cart.items[0]["price"], 1.0)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_add_multiple_items(self):
        self.cart.add_item("Apple", 1.0, 2)
        self.cart.add_item("Banana", 0.5, 3)
        self.assertEqual(len(self.cart.items), 2)

    def test_total_price(self):
        self.cart.add_item("Apple", 1.0, 2)
        self.cart.add_item("Banana", 0.5, 3)
        self.assertEqual(self.cart.total(), 3.5)

    def test_apply_discount(self):
        self.cart.add_item("Apple", 1.0, 2)
        self.cart.add_item("Banana", 0.5, 3)
        discounted_total = self.cart.apply_discount(20)
        self.assertAlmostEqual(discounted_total, 2.8, places=2)

    def test_apply_zero_discount(self):
        self.cart.add_item("Apple", 2.0, 1)
        self.assertEqual(self.cart.apply_discount(0), 2.0)

    def test_apply_full_discount(self):
        self.cart.add_item("Apple", 2.0, 1)
        self.assertEqual(self.cart.apply_discount(100), 0.0)

if __name__ == '__main__':
    unittest.main()
