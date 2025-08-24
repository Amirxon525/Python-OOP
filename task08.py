class Telefon:
    def __init__(self, model, narx):
        self.model = model
        self.narx = narx

tel1 = Telefon("iPhone 13", 9000000)
tel2 = Telefon("Samsung A52", 4500000)

print(tel1.model, "narxi", tel1.narx, "sum")
print(tel2.model, "narxi", tel2.narx, "sum")

