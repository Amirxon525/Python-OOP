class Kompyuter:
    def __init__(self, turi, operatsion_tizimi):
        self.turi = turi
        self.operatsion_tizimi = operatsion_tizimi

kom1 = Kompyuter("Noutbuk", "Windows 11")
kom2 = Kompyuter("Stol kompyuter", "Linux")

print(kom1.turi,  kom1.operatsion_tizimi)
print(kom2.turi,  kom2.operatsion_tizimi)
