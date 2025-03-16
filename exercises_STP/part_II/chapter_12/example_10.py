class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.colour = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = float(days * temp)

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 9.8)
print(orange.mold)

