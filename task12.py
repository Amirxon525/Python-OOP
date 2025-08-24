class Sportchi:
    def __init__(self, ism, sport_turi):
        self.ism = ism
        self.sport_turi = sport_turi

s1 = Sportchi("Hasan", "Boks")
s2 = Sportchi("Kamola", "Gimnastika")

print(s1.ism, s1.sport_turi)
print(s2.ism, s2.sport_turi)
