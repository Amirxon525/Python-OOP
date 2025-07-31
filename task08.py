class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ")
        else:
            print(f"{self.name} hozirda tugagan ")

p = Product("AirPods", 199.99, "electronics", True)
p.check_stock()
