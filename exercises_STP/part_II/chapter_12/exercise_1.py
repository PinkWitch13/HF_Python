"""1. Define a class called Apple with four 
    instance variables that represent four 
    attributes of an apple. """

class Apple:
    def __init__(self, weight, size, colour, sweetness ):
        self.weight = weight
        self.size = size
        self.colour = colour
        self.sweetness = sweetness

apple_1 = Apple(10, "normal", "green", "sweet")
apple_2 = Apple(13, "big", "dark red", "sweet")
apple_3 = Apple(8.5, "small", "yellow-pink", "sour")

print(apple_1.sweetness)
print(apple_2.size)
print(apple_3.colour)
