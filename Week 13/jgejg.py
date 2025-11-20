class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items else {}
    
    def add_item(self, item):
        self.items[item] = self.items.get(item, 0) + 1
    
    def __add__(self, other):
        result = ShoppingCart(self.items.copy())
        for item, qty in other.items.items():
            result.items[item] = result.items.get(item, 0) + qty
        return result
    
    def __str__(self):
        return str(self.items)

cart1 = ShoppingCart()
cart1.add_item("tea")
cart1.add_item("energy drink")
cart1.add_item("energy drink")
cart2 = ShoppingCart()
cart2.add_item("energy drink")
cart2.add_item("hat")
cart3 = cart1 + cart2
print(cart3)
