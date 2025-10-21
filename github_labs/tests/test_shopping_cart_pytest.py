# tests/test_shopping_cart_pytest.py
import pytest
from src.shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item(cart):
    cart.add_item("Apple", 1.0, 2)
    assert len(cart.items) == 1
    assert cart.items[0]["item_name"] == "Apple"

def test_remove_item(cart):
    cart.add_item("Banana", 0.5, 3)
    cart.remove_item("Banana")
    assert len(cart.items) == 0

def test_calculate_total(cart):
    cart.add_item("Apple", 1.0, 2)
    cart.add_item("Banana", 0.5, 3)
    assert cart.calculate_total() == 3.5

def test_apply_discount(cart):
    cart.add_item("Apple", 1.0, 2)
    cart.add_item("Banana", 0.5, 3)
    assert cart.apply_discount(20) == pytest.approx(2.8)

def test_invalid_price_or_quantity(cart):
    with pytest.raises(ValueError):
        cart.add_item("Orange", -1.0, 1)
    with pytest.raises(ValueError):
        cart.add_item("Orange", 1.0, -1)

def test_invalid_discount(cart):
    cart.add_item("Apple", 1.0, 2)
    with pytest.raises(ValueError):
        cart.apply_discount(120)
