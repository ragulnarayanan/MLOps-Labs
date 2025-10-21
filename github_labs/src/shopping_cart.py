# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price, quantity=1):
        if price < 0 or quantity < 1:
            raise ValueError("Price and quantity must be positive")
        self.items.append({"item_name": item_name, "price": price, "quantity": quantity})

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item["item_name"] != item_name]

    def calculate_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def apply_discount(self, discount_percentage):
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        total = self.calculate_total()
        return total * (1 - discount_percentage / 100)
