"""4. Create a class Horse and a class Rider. 
    Use composition to model a horse that has 
    a rider.   """

class Horse():
    def __init__ (self,
                  name,
                  colour,
                  size,
        rider):
        self.name = name
        self.colour = colour
        self.size = size 
        self.rider = rider

class Rider():
    def __init__ (self, name):
        self.name = name

rider = Rider("Bob Badger")
horse_1 = Horse("Tunder",
                 "black", 
                 "big horse",
                 rider)

print(horse_1.rider.name)
