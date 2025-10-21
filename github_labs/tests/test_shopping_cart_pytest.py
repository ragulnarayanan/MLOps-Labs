import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item(cart):
    cart.add_item("Apple", 1.0, 2)
    assert len(cart.items) == 1
    assert cart.items[0]["name"] == "Apple"

def test_total(cart):
    cart.add_item("Apple", 1.0, 2)
    cart.add_item("Banana", 0.5, 3)
    assert cart.total() == 3.5

def test_apply_discount(cart):
    cart.add_item("Apple", 1.0, 2)
    cart.add_item("Banana", 0.5, 3)
    assert pytest.approx(cart.apply_discount(20), 0.01) == 2.8

def test_empty_cart_total(cart):
    assert cart.total() == 0

def test_apply_full_discount(cart):
    cart.add_item("Orange", 3.0, 1)
    assert cart.apply_discount(100) == 0.0
