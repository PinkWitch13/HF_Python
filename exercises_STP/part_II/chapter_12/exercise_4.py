import random

"""4. Make a Hexagon class with a method 
    called calculate_perimeter that calculates 
    and returns its perimeter. Then create 
    a Hexagon object, call calculate_perimeter 
    on it, and print the result.  """

rand_1 = random.randint(0, 20)

class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_parameter(self):
        return 6 * self.side
    
hexa_1 = Hexagon(rand_1)

print(hexa_1.calculate_parameter())