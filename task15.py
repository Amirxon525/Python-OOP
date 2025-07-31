class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock


product1 = Product("Olma", 25.5, True)
product2 = Product("Banan", 18.0, False)
product3 = Product("Uzum", 30.0, True)
product4 = Product("Anor", 22.5, True)
product5 = Product("Gilos", 28.0, False)


products = [product1, product2, product3, product4, product5]


total_price = sum(p.price for p in products if p.in_stock)

print(f"Ombordagi mahsulotlar narxi: {total_price}")
