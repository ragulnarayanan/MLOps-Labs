class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def apply_discount(self, discount_percent):
        total_price = self.total()
        discount = total_price * (discount_percent / 100)
        return total_price - discount
