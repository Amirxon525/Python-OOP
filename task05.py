class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

p1 = Product("iPhone", 12999.99, "electronics", True)
p2 = Product("Keyboard", 59.99, "accessory", False)

print(p1.name, p1.price)
print(p2.name, p2.price)
